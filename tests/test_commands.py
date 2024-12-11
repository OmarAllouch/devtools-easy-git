from pathlib import Path
import pytest
from git import Repo
from src.git_utils import get_git_repo, get_changed_files


@pytest.fixture
def mock_repo(tmp_path):
    """Create a fresh Git repository for each test."""
    repo_path = tmp_path / "mock-repo"
    repo = Repo.init(repo_path)

    initial_file = repo_path / "README.md"
    initial_file.write_text("# Initial README\n")
    repo.index.add([str(initial_file)])
    repo.index.commit("Initial commit")
    yield repo


def test_get_git_repo():
    """Test that the get_git_repo function returns a Repo object."""
    repo = get_git_repo()
    assert isinstance(repo, Repo), "Expected a Repo object to be returned"


def test_no_changes(mock_repo):
    """Test that no changes are detected in a clean repo."""
    changed_files = get_changed_files(mock_repo)
    assert changed_files == [], "Expected no changed files in a clean repo"


def test_untracked_files(mock_repo):
    """Test that untracked files are detected."""
    new_file_path = Path(mock_repo.working_tree_dir) / "new_file.txt"
    new_file_path.write_text("Hello, world!")

    changed_files = get_changed_files(mock_repo)

    assert (
        "new_file.txt" in changed_files
    ), "Expected 'new_file.txt' to be in the list of changed files"
    assert len(changed_files) == 1, "Only one file should be in the list"


def test_modified_files(mock_repo):
    """Test that modified files are detected."""
    readme_path = Path(mock_repo.working_tree_dir) / "README.md"
    readme_path.write_text("# Modified README\n")

    changed_files = get_changed_files(mock_repo)

    assert (
        "README.md" in changed_files
    ), "Expected 'README.md' to be in the list of changed files"
    assert len(changed_files) == 1, "Only one file should be in the list"


def test_deleted_files(mock_repo):
    """Test that deleted files are detected."""
    readme_path = Path(mock_repo.working_tree_dir) / "README.md"
    readme_path.unlink()  # Delete the file

    changed_files = get_changed_files(mock_repo)

    assert (
        "README.md" in changed_files
    ), "Expected 'README.md' to be in the list of changed files"
    assert len(changed_files) == 1, "Only one file should be in the list"


def test_multiple_changes(mock_repo):
    """Test that multiple types of changes are detected (untracked + modified)."""
    untracked_file = Path(mock_repo.working_tree_dir) / "untracked_file.txt"
    untracked_file.write_text("This is untracked")

    readme_path = Path(mock_repo.working_tree_dir) / "README.md"
    readme_path.write_text("# Modified README\n")

    changed_files = get_changed_files(mock_repo)

    assert (
        "untracked_file.txt" in changed_files
    ), "Expected 'untracked_file.txt' to be in the list of changed files"
    assert (
        "README.md" in changed_files
    ), "Expected 'README.md' to be in the list of changed files"
    assert len(changed_files) == 2, "Two files should be in the list of changed files"
