import click

from screener.src.common.config import conf_key_save, conf_key_credentials, conf_key_imgur


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

    if save is not None:
        ctx.obj.conf.update(conf_key_save, save)

    if credentials is not None:
        ctx.obj.conf.update(conf_key_credentials, credentials)

    if imgur is not None:
        ctx.obj.conf.update(conf_key_imgur, imgur)

    click.echo(click.style("Params after update:", fg='bright_white'))
    click.echo(click.style("\nPath config: {}".format(ctx.obj.conf.path), fg='white'))

    with open(ctx.obj.conf.path, 'r') as file:
        click.echo('\n{}\n'.format(file.read().strip()))
