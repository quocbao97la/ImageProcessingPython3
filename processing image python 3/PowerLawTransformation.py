from pylab import *
import math, numpy
import scipy.misc
from scipy.misc.pilutil import Image
# opening the image and converting it to grayscale
a = Image.open('./images/obama.png').convert('L')
# a is converted to an ndarray
b = scipy.misc.fromimage(a)
# gamma is initialized
gamma = 0.5
# b is converted to type float
b1 = b.astype(float)
# maximum value in b1 is determined
b3 = numpy.max(b1)
# b1 is normalized
b2 = b1/b3
# gamma-correction exponent is computed
b3 = numpy.log(b2)*gamma
# gamma-correction is performed
c = numpy.exp(b3)*255.0
# c is converted to type int
c1 = c.astype(int)
# c1 is converted from ndarray to image
d = scipy.misc.toimage(c1)
# displaying the image

figure()
subplot(1,2,1), imshow(a), title("anh goc")
subplot(1,2,2), imshow(d), title("anh sau khi bien doi")
show()