import scipy.misc
import numpy, math
from scipy.misc.pilutil import Image
from pylab import *

# opening the image and converting it to grayscale

a = Image.open('./images/obama.png').convert('L')
# a is converted to an ndarray
b = scipy.misc.fromimage(a)
# b is converted to type float
b1 = b.astype(float)
# maximum value in b1 is determined
b2 = numpy.max(b1)
# performing the log transformation
c = (255.0*numpy.log(1+b1))/numpy.log(1+b2)
# c is converted to type int
c1 = c.astype(int)
# c1 is converted from ndarray to image
d = scipy.misc.toimage(c1)
figure()
subplot(1,2,1), imshow(a), title("anh goc")
subplot(1,2,2), imshow(d), title("LogTransformImage")
show()
# saving d as logtransform_output.png
#d.save('../Figures/logtransform_output.png')