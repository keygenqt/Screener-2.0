import subprocess
import time
from pathlib import Path

import click
import pyautogui
import pyperclip
from imgurpython import ImgurClient

from screener.src.common.select import select


@click.group(name='grab')
def cli_grab():
    """Take screenshot."""
    pass


@cli_grab.command()
@click.option('--delay', '-d', default=0, help='Delay take screenshot in sec. Default - 0.', type=click.INT, required=False)
@click.pass_context
def area(ctx, delay):
    """Take screenshot with select area."""
    time.sleep(delay)
    imgur = ctx.obj.get('imgur')
    ex = ctx.obj.get('extension')
    path = select(ctx.obj.get('save'), ex)
    if path != '':
        if imgur:
            pyperclip.copy(upload_imgur(path))
            click.echo('Added url the clipboard successfully.'.format(path))
        else:
            subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'image/{}'.format(ex), path])
            click.echo('Saved successfully: {}'.format(path))
            click.echo('Added to the clipboard successfully.'.format(path))


@cli_grab.command()
@click.option('--delay', '-d', default=0, help='Delay take screenshot in sec. Default - 0.', type=click.INT, required=False)
@click.pass_context
def desktop(ctx, delay):
    """Take screenshot full desktop."""
    time.sleep(delay)

    def get_count(value):
        return sum(1 for x in value.glob('**/*') if x.is_file())

    imgur = ctx.obj.get('imgur')
    save = ctx.obj.get('save')
    ex = ctx.obj.get('extension')
    path = '{}/{}.{}'.format(save, get_count(Path(save)) + 1, ex)
    s = pyautogui.screenshot()
    s.save(path)

    if path != '':
        if imgur:
            pyperclip.copy(upload_imgur(path))
            click.echo('Added url the clipboard successfully.'.format(path))
        else:
            subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'image/{}'.format(ex), path])
            click.echo('Saved successfully: {}'.format(path))
            click.echo('Added to the clipboard successfully.'.format(path))


def upload_imgur(path):
    return ImgurClient('de5c50f78fc633e', '----WebKitFormBoundary7MA4YWxkTrZu0gW').upload_from_path(path)['link']
