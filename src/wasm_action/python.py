"""
Python in a sandbox using WASM/WASI.

uvx --python 3.14 wasm-action python
"""

import os
import sys
import tempfile
import shutil
import enum

from . import cache
from . import lib
from .wasm import runtime


class Interpreter(enum.Enum):
    CPYTHON = "cpython"
    MONTY = "monty"


PYTHON = {
    "3.14": {
        "registry": "wa.dev",
        "package": "xelato:python314",
        "version": "26.2.6",
        "sha256": "6a9e23d3db2ea0883fb74bfe9540bcb27bd167be1dab39546a5376112f4beea0",
        "main": "_start",
    },
    "monty": {
        "registry": "wa.dev",
        "package": "xelato:monty",
        "version": "26.2.13",
        "sha256": "d611d5d22fd4cc475689b032e5c293f70428f59a48bd36b9006a8eaacfea5e59",
        "main": "_start",
    },
}


def run_python(args, interpreter: Interpreter = Interpreter.CPYTHON):
    if interpreter == Interpreter.MONTY:
        version = "monty"
    elif interpreter == Interpreter.CPYTHON:
        v = sys.version_info
        version = "{}.{}".format(v.major, v.minor)
    else:
        raise ValueError(f"unknown interpreter {interpreter}")

    python = PYTHON.get(version) or PYTHON["3.14"]

    if cache.exists(python["sha256"]):
        content = cache.fetch(python["sha256"])
    else:
        print(
            "Downloading {} with version {}".format(
                python["package"], python["version"]
            )
        )
        download = lib.pull(
            registry=python["registry"],
            package="{}@{}".format(python["package"], python["version"]),
        )
        if download.digest != "sha256:{}".format(python["sha256"]):
            raise ValueError("unexpected digest while downloading build")

        cache.store(download.content)
        content = download.content

    # stdlib: reuse host Python install
    stdlib = os.path.dirname(os.__file__)
    # sys.stdout.write("Using python stdlib {}\n".format(stdlib))
    guest_stdlib = "/usr/local/lib/python{}".format(version)

    tmp = tempfile.mkdtemp("py")

    # sysconfig data
    sysdata = """build_time_vars = {}\n""".format(
        repr(
            {
                # list only relevant build vars
                "exec_prefix": "/usr/local",
                "prefix": "/usr/local",
            }
        )
    )
    build = tempfile.mkdtemp("py")
    with open(os.path.join(build, "_sysconfigdata__wasi_wasm32-wasi.py"), "w") as f:
        f.write(sysdata)

    instance = (
        runtime.module(content)
        .wasi()
        # pass all cli arguments to the wasm "process"
        .argv(["python"] + [x for x in args])
        # configure python lib
        .env("PYTHONPATH", ":".join([guest_stdlib, "/build"]))
        # RO: stdlib
        .mount(stdlib, guest_stdlib, readonly=True)
        # RO: sysconfig data
        .mount(build, "/build", readonly=True)
        # RW: /tmp folder
        .mount(tmp, "/tmp", readonly=False)
        # RW: CWD for running user code.
        .mount(os.getcwd(), "/", readonly=False)
        .instance()
    )

    # todo: exit code?
    try:
        instance.function(python["main"])()
    finally:
        # clean-up
        shutil.rmtree(tmp)
        shutil.rmtree(build)
