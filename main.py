import os
import sys
import argparse
import re
import numpy

from stl_tools import numpy2stl, text2png
from scipy.ndimage import gaussian_filter
from pylab import imread
from PIL import Image
import PIL.ImageOps

MAX_HEIGHT = 200
MAX_WIDTH = 200
MAX_DEPTH = 40
OUTPUT_DIR = "stl_out/"
DEFAULT_INPUT_DIR = "inputs/"


def test_img2stl():
    A = 256 * imread("examples/helloWorld.png")
    A = A[:, :, 2] + 1.0*A[:, :, 0]  # Compose RGBA channels to give depth
    A = gaussian_filter(A, 1)  # smoothing
    numpy2stl(A,
              "examples/helloWorld.stl",
              max_height=MAX_HEIGHT,
              max_width=MAX_WIDTH,
              max_depth=MAX_DEPTH,
              scale=0.15,
              solid=True)


def test_txt2braille():
    print "TODO"


def test_braille2stl():
    print "TODO"


def process_input(file, args):
    if file.name.lower().endswith('.png'):
        process_image(file, args)
    elif file.name.lower().endswith('.txt'):
        process_text(file, args)
    else:
        print "All inputs must be .png or .txt. Skip"


def process_text(file, args):
    print "TODO: Processing text: %s" % file.name


def process_image(file, args):
    print "Processing image: %s" % file.name
    fname_pure = re.search('^(.+)/([^/]+).png', file.name)
    if args.inv is True:
        A = invert_image(file.name)
    else:
        A = 256 * imread(file.name)

    A = A[:, :, 2] + 0.5*A[:, :, 0]
    A = gaussian_filter(A, 2)  # smoothing
    numpy2stl(A,
              OUTPUT_DIR + fname_pure.group(2) + ".stl",
              scale=0.08,
              min_thickness_percent=0.2,
              solid=True)


def invert_image(file):
    return numpy.asarray(PIL.ImageOps.invert(Image.open(file)))


def process_args(args):
    if args.idir is not None:
        for path, dirs, files in os.walk(args.idir):
            for filename in files:
                fullname = os.path.join(path, filename)
                process_input(fullname, args)
                # result_fullname = os.path.join(args.dest, result_filename)

    elif len(args.inputs) != 0:
        for input_file in args.inputs:
            process_input(input_file, args)
    else:
        for path, dirs, files in os.walk(DEFAULT_INPUT_DIR):
            for filename in files:
                fullname = os.path.join(path, filename)
                process_input(fullname, args)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image/Braille text'
                                     ' converter to .STL')
    parser.add_argument('-t',
                        action='store_true',
                        help='runs all tests')
    parser.add_argument('-inv',
                        action='store_true',
                        help='inverts the picture colors')
    parser.add_argument('-idir',
                        help='the directory with inputs',
                        default=DEFAULT_INPUT_DIR)
    parser.add_argument('inputs',
                        nargs='*',
                        type=argparse.FileType('r'),
                        help='A list of inputs (.PNG, .TXT)')

    args = parser.parse_args()

    if args.t is True:  # Runs tests
        print "Running tests..."
        test_txt2braille()
        test_braille2img()
        test_img2stl()
    else:
        process_args(args)
