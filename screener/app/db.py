import click


@click.group(name='db')
def cli_db():
    """This script prints some colors.  If colorama is installed this will
    also work on Windows.  It will also automatically remove all ANSI
    styles if data is piped into a file.
    Give it a try!
    """
    pass


@cli_db.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def initdb(count, name):
    """This script prints some colors.  If colorama is installed this will
    also work on Windows.  It will also automatically remove all ANSI
    styles if data is piped into a file.
    Give it a try!
    """
    for x in range(count):
        click.echo('Hello %s!' % name)


@cli_db.command()
def dropdb():
    """This script prints some colors If colorama is installed this will
    also work on Windows.  It will also automatically remove all ANSI
    styles if data is piped into a file.
    Give it a try!
    """
    click.echo('Dropped the database')
