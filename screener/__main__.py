import click

from .src.commands.grab import cli_grab
from .src.commands.settings import cli_settings
from .src.common.config import Config

Config.init_conf()

@click.group()
@click.option('--test', help='For test', hidden=True, is_flag=True, default=False, is_eager=True)
@click.option('--dev', help='For configuration ./', hidden=True, is_flag=True, default=False, is_eager=True)
@click.pass_context
def cli(ctx, dev, test):
    """
        Application "screener" for easy screenshot.

        Take screenshots. Modify. Share. Unfamiliar
        language in the screenshot? - Translate
        it, or use the function to get the text.
    """
    if not hasattr(ctx.obj, 'test'):
        ctx.obj = Config(test, dev)


cli.add_command(cli_grab)
cli.add_command(cli_settings)

if __name__ == '__main__':
    cli(obj={})
