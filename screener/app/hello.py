import click


@click.group(name='hello')
def cli_hello():
    """This script prints some colors.  If colorama is installed this will
    also work on Windows.  It will also automatically remove all ANSI
    styles if data is piped into a file.
    Give it a try!
    """
    pass


@cli_hello.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)


@cli_hello.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello2(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)
