from test import run_tests
from processor import process_inputs


def run(parsed_args):
    if parsed_args.test:
        print('Running tests...')
        run_tests()
    else:
        print('Processing inputs...')
        process_inputs(parsed_args)
