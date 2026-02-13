import os
import sys
import click
import importlib.metadata
import json

from . import lib
from . import python
from .warg.crypto import generate_key
from .wasm import runtime
from .util import cli_error_handler


@click.group()
def cli():
    pass


@cli.command(help="Print version")
def version():
    try:
        version = importlib.metadata.version("wasm-action")
    except importlib.metadata.PackageNotFoundError:
        version = "0.0.0"
    print(version)


@cli.command(help="Push to registry")
@click.option("-r", "--registry", required=True, help="registry domain name")
@click.option("-p", "--package", required=True, help="package spec")
@click.option("--path", required=True, help="filename")
@click.option(
    "--warg-token",
    required=False,
    envvar="WARG_TOKEN",
    help="warg token (or $WARG_TOKEN)",
)
@click.option(
    "--warg-private-key",
    required=False,
    envvar="WARG_PRIVATE_KEY",
    help="warg private key (or $WARG_PRIVATE_KEY)",
)
@cli_error_handler
def push(registry, package, path, warg_token, warg_private_key):
    lib.push_file(
        registry=registry,
        package=package,
        path=path,
        warg_token=warg_token,
        warg_private_key=warg_private_key,
        cli=True,
    )


@cli.command(help="Pull from registry")
@click.option("-r", "--registry", required=True, help="registry domain name")
@click.option("-p", "--package", required=True, help="package spec")
@click.option("--path", required=False, help="filename")
@click.option(
    "--warg-token",
    required=False,
    envvar="WARG_TOKEN",
    help="warg token (or $WARG_TOKEN)",
)
@cli_error_handler
def pull(registry, package, path=None, warg_token=None):
    lib.pull_file(
        registry=registry,
        package=package,
        path=path,
        warg_token=warg_token,
        cli=True,
    )


@cli.command(help="Generate private key or read one from stdin")
@cli_error_handler
def key():
    """Generate key in json format.

    Either:
     - generate a new key
     - read a private key from standard input
    """
    if sys.stdin.isatty():
        data = generate_key()
    else:
        # read private key from standard input
        private_key = sys.stdin.read()
        data = generate_key(private_key)
        del data["private"]
    print(json.dumps(data, indent=4))


@cli.command("x", help="Run a WebAssembly file")
@click.argument("filename", required=True)
@click.argument("func", required=False)
@click.argument("args", nargs=-1)
@cli_error_handler
def run(filename, func, args):
    """Run a WebAssembly file"""

    print(runtime.module_file(filename).instance().function(func).call(*args))


@cli.command(
    "eval",
    help="""Expression evaluator

Expression(s) specified in EXPRESSION or STDIN will be evaluated against the specified WebAssembly module.
The input must conform to a subset of Python's syntax that includes literals, tuples and function calls.
The latter are resolved to a valid function present in the exports of the WebAssembly module.
Example:
If calc.wasm exports `add` and `mul`, then the following is a valid expression in such context:
"mul(2, 3), add(mul(4, 5), 3)"
""",
)
@click.argument("filename", required=True)
@click.argument("expression", required=False)
@cli_error_handler
def evaluate(filename, expression):
    """Evaluates an expression against a wasm module instance.

    Any function calls are intercepted and resolved to a valid function
    from the exports of the wasm module.

    Expression syntax follows a subset of Python syntax.

    """
    instance = runtime.module_file(filename).instance()

    expression = sys.stdin.read() if not sys.stdin.isatty() else expression

    if expression:
        for result in instance.evaluate(expression):
            print(result)
        return

    if not sys.stdin.isatty():
        return

    # repl mode
    import readline  # noqa

    prompt = "{} >>> ".format(os.path.basename(filename))
    while True:
        expression = input(prompt)
        try:
            for result in instance.evaluate(expression):
                print(result)
        except Exception as e:
            print(e)


@cli.command(
    "python",
    help="Python in a sandbox",
    context_settings=dict(
        ignore_unknown_options=True,
    ),
)
@click.option("--cpython", is_flag=True, help="Use python/cpython (default)")
@click.option("--monty", is_flag=True, help="Use pydantic/monty")
@click.argument("args", nargs=-1, type=click.UNPROCESSED)
@cli_error_handler
def run_python(cpython, monty, args):
    """Run a WASI-compiled wasm build of cpython"""
    python.run_python(args, kind="monty" if monty else None)


if __name__ == "__main__":
    cli()
