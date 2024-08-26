#!/usr/bin/env python3

import click
from greet import greet
from hello import hello

from commands.stop_instance import stop_instance
from commands.delete_snapshot import delete_snapshot

@click.group()
def cli():
    """A CLI tool with multiple commands."""
    pass

@cli.command()
@click.pass_context
def help(ctx):
    """Show this message and exit."""
    click.echo(ctx.parent.get_help())

@cli.command()
def version():
    """Display the version of mycli."""
    click.echo("mycli, version 1.0.0")

cli.add_command(greet)
cli.add_command(hello)
cli.add_command(stop_instance)
cli.add_command(delete_snapshot)

if __name__ == '__main__':
    cli()
