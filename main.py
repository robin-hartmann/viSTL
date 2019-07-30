import argparse

from stl_tools import numpy2stl, text2png
from scipy.ndimage import gaussian_filter
from pylab import imread


def test_img2stl_helloworld():
    A = 256 * imread("examples/helloWorld.png")
    A = A[:, :, 2] + 1.0*A[:, :, 0]  # Compose RGBA channels to give depth
    A = gaussian_filter(A, 1)  # smoothing
    numpy2stl(A,
              "examples/helloWorld.stl",
              max_height=200,
              max_width=200,
              max_depth=50,
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


def process_input(file):
    print "My file: %s" % file
    # TODO: distinguish between PNG and TXT


def validate_inputs(inputs):
    check = lambda fname: fname.lower().endswith(('png', 'txt'))
    for input_file in inputs:
        if not check(input_file.name):
            sys.stderr.write('All inputs must be .png or .txt')
            sys.exit(1)
        else:
            process_input(input_file.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image/Text (Braille) converter to .STL')
    parser.add_argument('-t',
                        action='store_true',
                        default=False,
                        help='runs all tests')
    parser.add_argument('inputs',
                        nargs='*',
                        type=argparse.FileType('r'),
                        help='A list of inputs (.PNG, .TXT)')
    args = parser.parse_args()

    if args.t is not None:  # Runs tests
        test_img2stl_helloworld()
        test_txt2stl_braille()
    else:
        validate_inputs(args.inputs)
