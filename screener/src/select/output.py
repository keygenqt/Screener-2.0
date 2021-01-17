import subprocess

import click
import pyperclip
from imgurpython import ImgurClient


class Output:
    @staticmethod
    def show(ctx, select_image):
        """Screenshot output."""
        imgur = ctx.obj.get('imgur')
        if select_image is not None:
            click.echo('{} {}'.format(click.style("Saved successfully:", fg='green'), select_image.path))
            if imgur:
                url = Output.upload_imgur(select_image)
                pyperclip.copy(url)
                click.echo('{} {}'.format(click.style("Added url the clipboard:", fg='green'), url))
            else:
                t = 'image/{}'.format((select_image.conf_extension, 'jpeg')[select_image.conf_extension == 'jpg'])
                subprocess.run(['xclip', '-t', t, '-se', 'c', select_image.path])
                click.echo(click.style("Image added to the clipboard successfully.", fg='green'))

    @staticmethod
    def upload_imgur(select_image):
        """Upload screenshot to imgur."""
        return ImgurClient('de5c50f78fc633e', '----WebKitFormBoundary7MA4YWxkTrZu0gW').upload_from_path(select_image.path)['link']
