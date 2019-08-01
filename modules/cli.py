import argparse
import os

from const import OUTPUT_DIR, DEFAULT_INPUT_DIR, DEFAULT_TABLE
from text2braille import text2braille
from unicode2png import unicode2png
from png2stl import png2stl
from test import run_tests
from util import get_new_fname


def process_text(fname_txt, parsed_args):
    print('Translating "%s" to braille...' % fname_txt)
    braille = text2braille(fname_txt, parsed_args.t)
    fname_png = get_new_fname(fname_txt, DEFAULT_INPUT_DIR, 'png')
    print('Rendering braille to png at "%s"' % fname_png)
    unicode2png(braille, fname_png)
    fname_stl = get_new_fname(fname_png, OUTPUT_DIR, 'stl')
    print('Converting png at "%s" to stl at "%s"' % (fname_png, fname_stl))
    png2stl(
        fname_png,
        fname_stl,
        should_invert=parsed_args.inv,
        smoothing=2,
        red_factor=4,
        scale=0.09
    )


def process_image(fname_png, parsed_args):
    fname_stl = get_new_fname(fname_png, OUTPUT_DIR, 'stl')
    print('Converting png at "%s" to stl at "%s"' % (fname_png, fname_stl))
    png2stl(
        fname_png,
        fname_stl,
        should_invert=parsed_args.inv,
        smoothing=2,
        red_factor=0.5,
        scale=0.08,
        min_thickness_percent=0.2
    )


def process_input(fname, parsed_args):
    print('Processing input: "%s"' % fname)
    if fname.lower().endswith('.png'):
        process_image(fname, parsed_args)
    elif fname.lower().endswith('.txt'):
        process_text(fname, parsed_args)
    else:
        print('All inputs must be .png or .txt, skipping...')


def process_inputs(parsed_args):
    if len(parsed_args.inputs) != 0:
        for input_file in parsed_args.inputs:
            process_input(input_file.name, parsed_args)
    else:
        for path, dirs, files in os.walk(DEFAULT_INPUT_DIR):
            for filename in files:
                fullname = os.path.join(path, filename)
                process_input(fullname, parsed_args)


def parse_args():
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

    return parser.parse_args()


def run(parsed_args):
    if parsed_args.test:
        print('Running tests...')
        run_tests()
    else:
        process_inputs(parsed_args)
