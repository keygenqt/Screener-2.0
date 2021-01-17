import time

import click

from screener.src.select.output import Output
from screener.src.select.select import Select


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
    image = Select(ctx).area()
    Output.show(ctx, image)


@cli_grab.command()
@click.option('--delay', '-d', default=0, help='Delay take screenshot in sec. Default - 0.', type=click.INT, required=False)
@click.pass_context
def desktop(ctx, delay):
    """Take screenshot full desktop."""
    time.sleep(delay)
    image = Select(ctx).desktop()
    Output.show(ctx, image)
