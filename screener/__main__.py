import click

from .src.commands.cloud import cli_cloud
from .src.commands.grab import cli_grab
from .src.commands.settings import cli_settings
from .src.common.config import Config


@click.group()
@click.option('--test', help='For test', hidden=True, is_flag=True, default=False, is_eager=True)
@click.option('--dev', help='For configuration ./', type=click.BOOL, default=False, hidden=True)
@click.pass_context
def cli(ctx, dev, test):
    """
        Application "screener" for easy screenshot.

        Take screenshots. Modify. Share. Unfamiliar
        language in the screenshot? - Translate
        it, or use the function to get the text.
    """
    # ctx.obj = Config(test, dev)
    if not hasattr(ctx.obj, 'test'):
        ctx.obj = Config(test, dev)


cli.add_command(cli_grab)
cli.add_command(cli_cloud)
cli.add_command(cli_settings)

if __name__ == '__main__':
    cli(obj={})
