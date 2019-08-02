#!/usr/bin/env python
from sys import argv
from modules.cli import parse_args, run as run_cli

if __name__ == '__main__':
    parsed_args = parse_args(argv[1:])

    # @todo
    # if parsed_args is not None:
    run_cli(parsed_args)
    # else:
    # run_gui
