#!/usr/bin/env python
from modules.cli import parse_args, run as run_cli

if __name__ == '__main__':
    parsed_args = parse_args()

    # @todo
    # if parsed_args is not None:
    run_cli(parsed_args)
    # else:
    # run_gui
