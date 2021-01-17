import click

from screener.src.common.config import conf_key_save, conf_key_imgur, conf_key_extension


@click.group(name='settings')
def cli_settings():
    """Configure the application via the command line."""
    pass


@cli_settings.command()
@click.option('--save', '-s', help='Update dir for save screenshots.', type=click.STRING, required=False)
@click.option('--imgur', '-i', help='Update imgur bool.', type=click.BOOL, required=False)
@click.option('--extension', '-e', help='Extension for save png/jpg.', type=click.STRING, required=False)
@click.pass_context
def update(ctx, save, imgur, extension):
    """Update configuration file params."""

    if save is None and imgur is None and extension is None:
        click.echo("Specify optionals for updating. Use --help for see optionals.")
        exit(0)

    if save is not None:
        ctx.obj.update(conf_key_save, save)

    if imgur is not None:
        ctx.obj.update(conf_key_imgur, imgur)

    if extension is not None:
        if extension != 'png' and extension != 'jpg':
            click.echo("Screenshot extension for save png/jpg!")
            exit(1)
        ctx.obj.update(conf_key_extension, extension)

    if not ctx.obj.test:
        click.echo(click.style("Params after update:", fg='bright_white'))
        click.echo(click.style("\nPath config: {}".format(ctx.obj.path), fg='white'))

    with open(ctx.obj.path, 'r') as file:
        click.echo('\n{}\n'.format(file.read().strip()))
