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


def test_img2stl_helloworld():
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


def test_txt2stl_braille():
    A = 256 * imread("examples/braille_inverse.png")
    A = A[:, :, 2] + 0.5*A[:, :, 0]  # Compose RGBA channels to give depth
    A = gaussian_filter(A, 2)  # smoothing
    numpy2stl(A,
              "examples/braille_inverse.stl",
              scale=0.05,
              mask_val=5.,
              solid=True)


def process_input(file, args):
    if file.name.lower().endswith('.png'):
        process_image(file, args)
    else:
        process_text(file, args)


def process_text(file, args):  # TODO
    print "Processing text: %s" % file.name


def process_image(file, args):
    print "Processing image: %s" % file.name
    fname_pure = re.search('^(.+)/([^/]+).png', file.name)
    if args.i is True:
        print "Inverting image..."
        A = 256 * invert_image(file.name)
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


def validate_inputs(args):
    check = lambda fname: fname.lower().endswith(('.png', '.txt'))
    for input_file in args.inputs:
        if not check(input_file.name):
            sys.stderr.write('All inputs must be .png or .txt')
            sys.exit(1)
        else:
            process_input(input_file, args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image/Braille text'
                                     ' converter to .STL')
    parser.add_argument('-t',
                        action='store_true',
                        help='runs all tests')
    parser.add_argument('-i',
                        action='store_true',
                        help='inverts the picture colors')
    parser.add_argument('inputs',
                        nargs='*',
                        type=argparse.FileType('r'),
                        help='A list of inputs (.PNG, .TXT)')
    args = parser.parse_args()

    if args.t is True:  # Runs tests
        print "Running tests..."
        test_img2stl_helloworld()
        test_txt2stl_braille()
    else:
        validate_inputs(args)
