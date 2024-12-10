import questionary
from git_utils import get_git_repo, get_origin, pull_changes


def sync() -> None:
    """Pulls changes from the remote and rebases them."""
    repo = get_git_repo()

    origin = get_origin(repo)

    branch = questionary.select(
        "Select the branch to sync with the remote",
        choices=[branch.name for branch in repo.branches],
        use_jk_keys=True,
    ).ask()

    pull_changes(origin, branch)
