import click


@click.group(name='grab')
def cli_grab():
    """Take screenshot."""
    pass


@cli_grab.command()
@click.option('--delay', '-d', default=0, help='Delay take screenshot in sec. Default - 0.', type=click.INT, required=False)
@click.pass_context
def select(ctx, delay):
    """Select area."""
    click.echo(click.style(ctx.obj.conf.get('save'), fg='blue'))
