import click


@click.group(name='platform')
def cli_cloud():
    """Take screenshot for Google Cloud Platform feature."""
    pass


@cli_cloud.command()
@click.option('--language', '-l', help='Language to translate.', type=click.STRING, required=True)
@click.pass_context
def translate(ctx, language):
    """Translate area."""
    click.echo(click.style(ctx.obj.conf.get('save'), fg='blue'))
