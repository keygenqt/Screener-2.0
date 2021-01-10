import click

from db import cli_db
from hello import cli_hello
from screenshot import cli_screenshot


@click.group()
def cli():
    pass


cli.add_command(cli_db)
cli.add_command(cli_hello)
cli.add_command(cli_screenshot)

if __name__ == '__main__':
    cli()
