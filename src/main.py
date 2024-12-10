#!/usr/bin/env python3
import click
from cli import qc, sc
from utils.helpers import AliasedGroup


@click.group(cls=AliasedGroup)
def cli():
    """easy-git: Simplify your Git workflows."""
    pass


@cli.command()
def quick_commit():
    """Interactive add-commit cycle."""
    qc()


@cli.command()
def sync():
    """Pull changes from the remote and rebase them."""
    sc()


if __name__ == "__main__":
    cli()
