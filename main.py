#!/usr/bin/env python
from sys import argv
from modules.cli import run as run_cli
from modules.args_parser import parse_args

if __name__ == '__main__':
    parsed_args = parse_args(argv[1:])

    # @todo
    # if parsed_args is not None:
    run_cli(parsed_args)
    # else:
    # run_gui
