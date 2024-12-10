import click
import questionary
from git_utils import (
    commit,
    get_git_repo,
    get_changed_files,
    add_file,
    push,
)


def quick_commit() -> None:
    repo = get_git_repo()

    # Step 1: Get the list of changed files
    changed_files = get_changed_files(repo)

    if not changed_files:
        click.echo("No changes to commit!")
        return

    # Step 2: Select files using questionary's checkbox
    selected_files = questionary.checkbox(
        "Select files to stage (use 'a' to toggle all, 'j'/'k' to navigate):",
        choices=[{"name": file} for file in changed_files],
        validate=lambda answers: "You must select at least one file."
        if not answers
        else True,
        use_jk_keys=True,
        instruction="(space to select, 'a' to toggle all)",
    ).ask()

    if not selected_files:
        click.echo("No files selected.")
        return

    # Step 3: Add the selected files
    for file in selected_files:
        add_file(repo, file)
    click.echo("Files staged successfully!")

    # Step 4: Get commit message or amend
    commit_type = questionary.select(
        "Choose commit type:", choices=["New Commit", "Amend Last Commit"]
    ).ask()

    if commit_type == "New Commit":
        commit_message = click.prompt("Enter commit message")
        commit(repo, commit_message, False)

    elif commit_type == "Amend Last Commit":
        commit(repo, "", True)
        click.echo("Amended the last commit.")

    # Step 5: Push changes
    push_choice = questionary.confirm(
        "Would you like to push now?", auto_enter=False
    ).ask()
    if push_choice:
        push(repo)
    else:
        click.echo("Skipped pushing.")
