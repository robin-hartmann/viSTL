import argparse

from const import DEFAULT_INPUT_DIR, DEFAULT_TABLE


def parse_args(args):
    parser = argparse.ArgumentParser(description='Image/Braille text'
                                     ' converter to .STL')
    parser.add_argument('-t',
                        help='the table to use for braille translation',
                        type=str,
                        default=DEFAULT_TABLE)
    parser.add_argument('-test',
                        action='store_true',
                        help='run all tests')
    parser.add_argument('-inv',
                        action='store_true',
                        help='invert the picture colors')
    parser.add_argument('-d',
                        help='the directory with inputs',
                        type=str,
                        default=DEFAULT_INPUT_DIR)
    parser.add_argument('inputs',
                        nargs='*',
                        type=argparse.FileType('r'),
                        help='A list of inputs (.PNG, .TXT)')

    return parser.parse_args(args)
