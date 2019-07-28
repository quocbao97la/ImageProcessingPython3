import scipy.misc
from scipy.misc.pilutil import Image
from pylab import *
from skimage import filters

# opening the image and converting it to grayscale
a = Image.open('./images/obama.png').convert('L')
# performing Sobel filter
b = filters.roberts(a)
# b is converted froma an ndarray to an image
b = scipy.misc.toimage(b)
figure()
subplot(1,2,1), imshow(a), title("original Image")
subplot(1,2,2), imshow(b), title("Robert Edge Detection")
show()