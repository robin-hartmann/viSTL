from const import MAX_WIDTH, MAX_HEIGHT, MAX_DEPTH
from numpy import asarray
from PIL import Image, ImageOps
from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl


def invert_image(fname):
    return asarray(ImageOps.invert(Image.open(fname)))


def png2stl(fname_png, fname_stl, should_invert=False, smoothing=0, red_factor=1, scale=0.1, min_thickness_percent=0.1):
    if should_invert:
        data = invert_image(fname_png)
    else:
        data = 256 * imread(fname_png)

    data = data[:, :, 2] + red_factor * data[:, :, 0]  # Compose RGBA channels to give depth -> B + red_factor * R
    data = gaussian_filter(data, smoothing)
    numpy2stl(
        data,
        fname_stl,
        scale=scale,
        max_width=MAX_WIDTH,
        max_height=MAX_HEIGHT,
        max_depth=MAX_DEPTH,
        solid=True,
        min_thickness_percent=min_thickness_percent,
    )
