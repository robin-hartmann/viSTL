from const import MAX_WIDTH, MAX_HEIGHT, MAX_DEPTH
from numpy import asarray
from PIL import Image, ImageOps
from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl


def invert_image(fname):
    im = Image.open(fname)
    if im.mode == 'RGB':
        return asarray(ImageOps.invert(im))
    else:
        print('Inversion for RGBA: Not yet implemented')
        return asarray(im)

# be careful:
# max_width and max_depth specify the area of the base
# and max_height specifies the height of the model
def png2stl(fname_png, fname_stl, should_invert=False, smoothing=0, red_factor=1, scale=0.1, min_thickness_percent=0.1,
            max_width=MAX_WIDTH, max_height=MAX_HEIGHT, max_depth=MAX_DEPTH):
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
        max_width=max_width,
        max_height=max_height,
        max_depth=max_depth,
        solid=True,
        min_thickness_percent=min_thickness_percent,
    )
