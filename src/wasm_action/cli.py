import sys
import click
import importlib.metadata
import json

from . import lib
from .warg.crypto import generate_key


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
@click.option('--registry', required=True, help="registry domain name")
@click.option('--package', required=True, help="package spec")
@click.option('--path', required=True, help="filename")
@click.option('--warg-token', required=False, envvar='WARG_TOKEN', help="warg token (or $WARG_TOKEN)")
@click.option('--warg-private-key', required=False, envvar='WARG_PRIVATE_KEY', help="warg private key (or $WARG_PRIVATE_KEY)")
def push(registry, package, path, warg_token, warg_private_key):

    try:

        lib.push_file(
            registry=registry,
            package=package,
            path=path,
            warg_token=warg_token,
            warg_private_key=warg_private_key,
            cli=True,
        )

    except Exception as e:
        print(e)
        sys.exit(1)


@cli.command(help="Pull from registry")
@click.option('--registry', required=True, help="registry domain name")
@click.option('--package', required=True, help="package spec")
@click.option('--path', required=False, help="filename")
@click.option('--warg-token', required=False, envvar='WARG_TOKEN', help="warg token (or $WARG_TOKEN)")
def pull(registry, package, path=None, warg_token=None):

    try:

        lib.pull_file(
            registry=registry,
            package=package,
            path=path,
            warg_token=warg_token,
            cli=True,
        )

    except Exception as e:
        print(e)
        sys.exit(1)


@cli.command(help="Generate private key or read one from stdin")
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
        del data['private']
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    cli()
