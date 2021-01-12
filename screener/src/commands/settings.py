import click


@click.group(name='settings')
@click.pass_context
def cli_settings(ctx):
    """Configure the application via the command line."""
    pass


@cli_settings.command()
@click.option('--save', '-s', help='Update dir for save screenshots.', type=click.STRING, required=False)
@click.option('--credentials', '-c', help='Update path credentials file google cloud.', type=click.STRING, required=False)
@click.option('--imgur', '-i', help='Update imgur bool.', type=click.BOOL, required=False)
@click.pass_context
def update(ctx, save, credentials, imgur):
    """Update configuration file params."""

    if save is None and credentials is None and imgur is None:
        click.echo("Specify optionals for updating. Use --help for see optionals.")
        exit(0)

    click.echo(click.style("Params after update:", fg='bright_white'))
    click.echo("   save: {}".format(ctx.obj.conf.get('save')))
    click.echo("   credentials: {}".format(ctx.obj.conf.get('credentials')))
    click.echo("   imgur: {}".format(ctx.obj.conf.get('imgur')))
