# from PIL import Image
#
# col = Image.open("obama.png")
# gray = col.convert('L')
# bw = gray.point(lambda x: 0 if x<128 else 255, '1')
# bw.save("result_bw.png")

import scipy.misc, numpy
from skimage import filters
from scipy.misc.pilutil import Image
from pylab import*
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage.morphology import label
from scipy.misc.pilutil import Image
from skimage.measure import regionprops
from skimage.filters import threshold_otsu
# opening the image and converting it to grayscale
a = Image.open('./images/obama.png').convert('L')
# a is converted to an ndarray
a = scipy.misc.fromimage(a)
# threshold value is determined by
# using Otsu's method
thresh = threshold_otsu(a)
# the pixels with intensity greater than
# theshold are kept
b = a > thresh
# labelling is performed on b
c = label(b)
# c is converted from an ndarray to an image
c1 = scipy.misc.toimage(c)
# c1 is saved as label_output.png
imshow(c1)
show()
#c1.save('../Figures/label_output.png')