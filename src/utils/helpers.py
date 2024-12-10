import os
import sys
import click
import signal


def is_git_repository() -> bool:
    """Check if the current directory is a Git repository."""
    return os.path.isdir(".git")


def confirm_action(message: str) -> bool:
    """Prompt the user to confirm an action."""
    response = input(f"{message} (y/n): ")
    return response.lower() == "y"


def handle_kill_signal(signal_number, frame):
    """Handle kill signals"""
    if signal_number in [signal.SIGINT, signal.SIGTERM]:
        click.echo("\nReceived interrupt signal. Exiting...")
        sys.exit(0)


# Register signal handlers
signal.signal(signal.SIGINT, handle_kill_signal)
signal.signal(signal.SIGTERM, handle_kill_signal)


aliases = {
    "c": "quick-commit",
    "h": "help",
}


class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx) if aliases.get(cmd_name) == x]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail(f"Too many matches: {', '.join(sorted(matches))}")

    def resolve_command(self, ctx, args):
        # always return the full command name
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name if cmd is not None else "", cmd, args
