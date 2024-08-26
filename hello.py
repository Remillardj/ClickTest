import click

@click.command()
def hello():
    """Prints 'Hello, World!'."""
    click.echo("Hello, World!")
