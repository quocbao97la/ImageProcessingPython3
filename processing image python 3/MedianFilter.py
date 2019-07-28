import scipy.misc
import scipy.ndimage
from scipy.misc.pilutil import Image
from pylab import *

# opening the image and converting it to grayscale
a = Image.open('./images/obama.png').convert('L')
figure()
subplot(1,2,1), imshow(a), title("original Image")
# performing the median filter
b = scipy.ndimage.filters.median_filter(a,size=5,
footprint=None,output=None,mode='reflect', cval=0.0,origin=0)
# b is converted from an ndarray to an image
b = scipy.misc.toimage(b)
subplot(1,2,2), imshow(b), title("Median filter")
#b.save('median_output.png')
show()