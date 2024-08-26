import click

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option('--greeting', default='Hello', help='Greeting word to use.')
def greet(name, greeting):
    """Greet someone with a custom message."""
    click.echo(f"{greeting}, {name}!")
