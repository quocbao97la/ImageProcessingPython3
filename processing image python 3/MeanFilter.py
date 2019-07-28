import numpy as np
import scipy.ndimage
from pylab import *
from scipy.misc.pilutil import Image
# opening the image and converting it to grayscale
a = Image.open('./images/obama.png').convert('L')
figure()
subplot(1,2,1)
imshow(a), title("anh goc")
k = np.ones((5,5))/25
# performing convolution
b = scipy.ndimage.filters.convolve(a, k)
# b is converted from an ndarray to an image
b = scipy.misc.toimage(b)
subplot(1,2,2)
imshow(b), title("anh duoc loc trung binh 5*5")
show()