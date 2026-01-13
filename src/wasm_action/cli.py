import sys
import click

from . import lib

@click.group()
def cli():
    pass


@cli.command(help="Push to registry")
@click.option('--registry', required=True, help="registry domain name")
@click.option('--package', required=True, help="package spec")
@click.option('--path', required=True, help="filename")
@click.option('--warg-token', required=False, envvar='WARG_TOKEN', help="warg token")
@click.option('--warg-private-key', required=False, envvar='WARG_PRIVATE_KEY', help="warg private key")
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
@click.option('--warg-token', required=False, envvar='WARG_TOKEN', help="warg token")
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


if __name__ == "__main__":
    cli()
