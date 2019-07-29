from stl_tools import numpy2stl, text2png

from scipy.ndimage import gaussian_filter
from pylab import imread


A = 256 * imread("examples/braille_inverse.png")
A = A[:, :, 2] + 0.5*A[:,:, 0] # Compose RGBA channels to give depth
A = gaussian_filter(A, 2)  # smoothing

numpy2stl(A, "examples/braille_inverse.stl", scale=0.05, mask_val=5., solid=True)



