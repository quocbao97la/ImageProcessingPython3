import math
import scipy.misc
import numpy as np
from scipy.misc.pilutil import Image
from pylab import *

# opening the image and converting it to grayscale
im = Image.open('./images/obama.png').convert('L')
# im is converted to an ndarray
im1 = scipy.misc.fromimage(im)
figure()
subplot(1,2,1),imshow(im), title('anh goc')
# performing the inversion operation
im2 = 255 - im1
# im2 is converted from an ndarray to an image
im3 = scipy.misc.toimage(im2)
subplot(1,2,2), imshow(im3),title("anh am ban")
show()
# saving the image as imageinverse_output.png in
# Figures folder
#im3.save('../Figures/imageinverse_output.png')