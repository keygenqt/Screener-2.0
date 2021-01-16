import click
import pyperclip

from screener.src.common.select import select


@click.group(name='grab')
def cli_grab():
    """Take screenshot."""
    pass


@cli_grab.command()
@click.option('--delay', '-d', default=0, help='Delay take screenshot in sec. Default - 0.', type=click.INT, required=False)
@click.pass_context
def area(ctx, delay):
    """Select area."""
    path = select(ctx.obj.get('save'), ctx.obj.get('extension'))
    if path != '':
        with open(path, 'rb') as f:
            pyperclip.copy('The text to be copied to the clipboard.')
            pyperclip.paste()
