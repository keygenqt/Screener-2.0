import click

from .src.commands.cloud import cli_cloud
from .src.commands.settings import cli_settings
from .src.commands.grab import cli_grab
from .src.common.config import Config


class App(object):
    conf = None
    dev = None

    def __init__(self, dev=False):
        self.conf = Config(dev)
        self.dev = dev


@click.group()
@click.option('--dev', help='For configuration ./', type=click.BOOL, default=False, hidden=True)
@click.pass_context
def cli(ctx, dev):
    """
        Application "screener" for easy screenshot.

        Take screenshots. Modify. Share. Unfamiliar
        language in the screenshot? - Translate
        it, or use the function to get the text.
    """
    ctx.obj = App(dev)


cli.add_command(cli_grab)
cli.add_command(cli_cloud)
cli.add_command(cli_settings)

if __name__ == '__main__':
    cli(obj={})
