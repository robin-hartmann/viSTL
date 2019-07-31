from numpy import asarray
from os import path
from PIL import Image, ImageOps
from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl


def invert_image(fname):
    return asarray(ImageOps.invert(Image.open(fname)))


def png2stl(fname, output_dir, should_invert=False, smoothing=0, red_factor=1, scale=0.1, min_thickness_percent=0.1):
    if should_invert:
        data = invert_image(fname)
    else:
        data = 256 * imread(fname)

    data = data[:, :, 2] + red_factor * data[:, :, 0]  # Compose RGBA channels to give depth -> B + red_factor * R
    data = gaussian_filter(data, smoothing)
    out_fname = path.splitext(path.basename(fname))[0] + ".stl"
    numpy2stl(
        data,
        output_dir + out_fname,
        scale=scale,
        max_width=200,
        max_height=200,
        max_depth=40,
        solid=True,
        min_thickness_percent=min_thickness_percent,
    )
