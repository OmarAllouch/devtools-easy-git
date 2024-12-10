import os
import sys
import click
from git import Repo, GitCommandError


def get_git_repo():
    """Return the current Git repository."""
    try:
        return Repo(os.getcwd())
    except Exception:
        click.echo("Not a git repository.")
        sys.exit(1)


def get_changed_files(repo: Repo) -> list[str]:
    """Return the list of changed files in the repository."""
    changed_files = [item.a_path for item in repo.index.diff(None)]  # Unstaged files
    changed_files += repo.untracked_files  # Untracked files
    return changed_files


def add_file(repo: Repo, file: str) -> None:
    """Add the given file to the staging area."""
    repo.git.add(file)


def commit(repo: Repo, message: str, amend: bool) -> None:
    """Commit the staged changes with the given message."""
    repo.git.commit(m=message) if not amend else repo.git.commit("--amend", "--no-edit")


def push(repo: Repo) -> None:
    """Push the changes to the remote repository."""
    try:
        repo.git.push()
        click.echo("Pushed to the remote repository.")
    except GitCommandError:
        click.echo("Error: Unable to push. Check your remote settings.")
