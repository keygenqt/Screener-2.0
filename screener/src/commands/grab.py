import click

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
    click.echo(click.style(select(), fg='blue'))
