import scipy.misc
import scipy.ndimage
from scipy.misc.pilutil import Image
from pylab import *

# opening the image and converting it to grayscale
a = Image.open('./images/obama.png').convert('L')
figure()
subplot(1,2,1), imshow(a), title("original Image")
# performing the median filter
b = scipy.ndimage.filters.gaussian_filter(a,sigma=5)
# b is converted from an ndarray to an image
b = scipy.misc.toimage(b)
subplot(1,2,2), imshow(b), title("Gaussian filter")
#b.save('median_output.png')
show()