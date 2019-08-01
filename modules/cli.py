import argparse
import os

from const import OUTPUT_DIR, DEFAULT_INPUT_DIR
from text2braille import text2braille
from unicode2png import unicode2png
from png2stl import png2stl
from test import run_tests


def process_text(fname, parsed_args):
    text = open(fname, "r").read()
    braille = text2braille(text)
    png = unicode2png(braille)
    png2stl(
        png,
        OUTPUT_DIR,
        should_invert=parsed_args.inv,
        smoothing=2,
        red_factor=4,
        scale=0.09
    )


def process_image(fname, parsed_args):
    png2stl(
        fname,
        OUTPUT_DIR,
        should_invert=parsed_args.inv,
        smoothing=2,
        red_factor=0.5,
        scale=0.08,
        min_thickness_percent=0.2
    )


def process_input(fname, parsed_args):
    print("Processing input: %s" % fname)
    if fname.lower().endswith('.png'):
        process_image(fname, parsed_args)
    elif fname.lower().endswith('.txt'):
        process_text(fname, parsed_args)
    else:
        print("All inputs must be .png or .txt, skipping...")


def process_inputs(parsed_args):
    if len(parsed_args.inputs) != 0:
        for input_file in parsed_args.inputs:
            process_input(input_file, parsed_args)
    else:
        for path, dirs, files in os.walk(DEFAULT_INPUT_DIR):
            for filename in files:
                fullname = os.path.join(path, filename)
                process_input(fullname, parsed_args)


def parse_args():
    parser = argparse.ArgumentParser(description='Image/Braille text'
                                     ' converter to .STL')
    parser.add_argument('-t',
                        action='store_true',
                        help='runs all tests')
    parser.add_argument('-inv',
                        action='store_true',
                        help='inverts the picture colors')
    parser.add_argument('-d',
                        help='the directory with inputs',
                        default=DEFAULT_INPUT_DIR)
    parser.add_argument('inputs',
                        nargs='*',
                        type=argparse.FileType('r'),
                        help='A list of inputs (.PNG, .TXT)')

    return parser.parse_args()


def run(parsed_args):
    if parsed_args.t:
        print("Running tests...")
        run_tests()
    else:
        process_inputs(parsed_args)
