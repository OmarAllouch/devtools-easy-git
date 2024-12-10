#!/usr/bin/env python3
import click
from cli import qc
from utils.helpers import AliasedGroup


@click.group(cls=AliasedGroup)
def cli():
    """easy-git: Simplify your Git workflows."""
    pass


@cli.command()
def quick_commit():
    """Interactive add-commit cycle."""
    qc()


if __name__ == "__main__":
    cli()
