#!/usr/bin/env python3
import sys
from pathlib import Path

import click

from jefferson.jffs2 import extract_jffs2


@click.command(
    help="A tool to extract JFFS2 filesystems.",
    context_settings=dict(help_option_names=["--help", "-h"]),
)
@click.argument(
    "file",
    type=click.Path(path_type=Path, dir_okay=False, exists=True, resolve_path=True),
    required=True,
)
@click.option(
    "-d",
    "--dest",
    type=click.Path(path_type=Path, dir_okay=True, file_okay=False, resolve_path=True),
    default=Path.cwd().joinpath("jffs2-root"),
    help="Extract the files to this directory. Will be created if doesn't exist.",
)
@click.option(
    "-f",
    "--force",
    is_flag=True,
    show_default=True,
    help="Force extraction even if outputs already exist (they are removed).",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Verbosity level, counting, maximum level: 3 (use: -v, -vv, -vvv)",
)
def cli(
    file: Path,
    dest: Path,
    force: bool,
    verbose: int,
) -> int:
    if dest.exists() and not force:
        print("Destination path already exists!")
        return -1
    dest.mkdir(exist_ok=True)
    return extract_jffs2(file, dest, verbose)


def main():
    try:
        ctx = cli.make_context("jefferson", sys.argv[1:])
    except click.ClickException as e:
        e.show()
        sys.exit(e.exit_code)
    except click.exceptions.Exit as e:
        sys.exit(e.exit_code)
    except Exception as e:
        print("Unhandled exception during jefferson", e)
        sys.exit(1)

    retval = 0
    try:
        with ctx:
            retval = cli.invoke(ctx)
    except Exception as e:
        print("Unhandled exception during jefferson", e)
        sys.exit(1)

    sys.exit(retval)


if __name__ == "__main__":
    main()
