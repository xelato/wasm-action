
"""
Python in a sandbox using WASM/WASI.

uvx --python 3.14 wasm-action python
"""

import os
import sys
import tempfile
import shutil

from . import cache
from . import lib
from .wasm import runtime

PYTHON = {

    '3.14': {
        'registry': 'wa.dev',
        'package': 'xelato:python314',
        'version': '26.2.6',
        'sha256': '6a9e23d3db2ea0883fb74bfe9540bcb27bd167be1dab39546a5376112f4beea0',
    },

}


def run_python(args):
    v = sys.version_info
    version = "{}.{}".format(v.major, v.minor)
    python = PYTHON.get(version) or PYTHON['3.14']

    if cache.exists(python['sha256']):
        print("Found object in cache")
        content = cache.fetch(python['sha256'])
    else:
        print("Downloading python build")
        download = lib.pull(
            registry=python['registry'],
            package="{}@{}".format(python['package'], python['version'])
        )
        if download.digest != "sha256:{}".format(python['sha256']):
            raise ValueError('unexpected digest while downloading build')

        cache.store(download.content)
        print("Stored object in local cache")
        content = download.content

    # Lib folder
    # Reusing the host Python installation
    python_lib = os.path.dirname(os.__file__)
    print("Using python lib {}".format(python_lib))

    argv = ['python']
    argv.extend(args)

    tmp = tempfile.mkdtemp('py')

    instance = (runtime
        .module(content)
        .wasi()
        # pass all cli arguments to the wasm "process"
        .argv(argv)

        # configure python lib
        .env('PYTHONPATH', '/lib:/build')
        .mount(python_lib, '/lib', readonly=True)

        # todo: ModuleNotFoundError: No module named '_sysconfigdata__wasi_wasm32-wasi'
        #.mount('{}/github/python/cpython/builddir/wasi/build/lib.wasi-wasm32-3.14'.format(os.environ['HOME']), '/build')

        # provide a /tmp folder
        .mount(tmp, '/tmp', readonly=False)

        # Get access to CWD for running user code.
        # note: it may be preferable to set this to a subdir of /
        .mount(os.getcwd(), "/", readonly=True)

        .instance()
    )

    # todo: exit code?
    try:
        instance.function('_start')()
    finally:
        # clean-up tmp dir
        shutil.rmtree(tmp)

    """
    https://github.com/python/cpython/blob/main/Modules/getpath.py
    Could not find platform independent libraries <prefix>
    Could not find platform dependent libraries <exec_prefix>
    """

    # 3.14
    """
    Installations of Python now contain a new file, :file:`build-details.json`.
    This is a static JSON document containing build details for CPython,
    to allow for introspection without needing to run code.
    This is helpful for use-cases such as Python launchers, cross-compilation,
    and so on.

    :file:`build-details.json` must be installed in the platform-independent
    standard library directory. This corresponds to the :ref:`'stdlib'
    <installation_paths>` :mod:`sysconfig` installation path,
    which can be found by running ``sysconfig.get_path('stdlib')``.
    """
