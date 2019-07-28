import scipy.misc
import scipy.ndimage
from scipy.misc.pilutil import Image
from pylab import *
import numpy as np
from PIL import Image, ImageFilter
# opening the image and converting it to grayscale
a =Image.open('./images/obama.png').convert('L')
# performing Laplacian filter

b= a.filter(ImageFilter.CONTOUR)

# b is converted from an ndarray to an image
b = scipy.misc.toimage(b)
figure()
subplot(1,2,1), imshow(a), title("original Image")
subplot(1, 2, 2), imshow(b), title("Laplican Filter")
show()
#b.save('../Figures/laplacian_new.png')