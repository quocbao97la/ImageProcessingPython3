
import numpy as np
from scipy.misc.pilutil import Image
from skimage import filters
from PIL import Image
from PIL import ImageFilter
from PIL import Image, ImageFilter
from skimage import io
from pylab import *
import scipy.misc
#read file to folder have name images 
im = Image.open('input.png')

im1= im.filter(ImageFilter.CONTOUR)
#show image on figure 
figure()
subplot(2,4,1),imshow(im),title("original image")
axis('off')
subplot(2,4,2), imshow(im1), title("Laplican Image")
axis('off')
im1arr = asarray(im,dtype=uint8)
im2arr = asarray(im1, dtype=uint8)

im2= im1arr - im2arr

im2 = scipy.misc.toimage(im2)

subplot(2,4,3), imshow(im2), title("c:Subtracting (a) and (b)")
axis('off')
im3 = filters.sobel(im)
# b is converted fimrom an ndarray to an image
im3= scipy.misc.toimage(im3)
subplot(2,4,4), imshow(im3), title("d Sobel ")
axis('off')

# --Image (d) smoothed with a 5*5 averaging filter

k = np.ones((5,5))/25
# performing convolution
im4 = scipy.ndimage.filters.convolve(im3, k)
# b is converted from an ndarray to an image
im4 = scipy.misc.toimage(im4)
subplot(2,4,5), imshow(im4), title("e 5*5 averaging filter ")
axis('off')


# -- The product of (c) and (e) which will be used as a mask
# im2 =asarray(im2)
# im4 =asarray(im4)
from PIL import ImageChops

im5 = ImageChops.multiply(im2,im4)
#im5=im2*im4;
im5 = scipy.misc.toimage(im5)

subplot(2,4,6),imshow(im5),title('f.The product of (c) and (e)');
axis('off')



#--Sharpened image which is sum of (a) and (f)
im6=im1arr+im5;

subplot(2,4,7),io.imshow(im6),title('g. sum of (a) and (f)');
axis('off')


# gamma is initialized
gamma = 0.5
# b is converted to type float
b1 = im6.astype(float)
# maximum value in b1 is determined
b3 = np.max(b1)
# b1 is normalized
b2 = b1/b3
# # gamma-correction exponent is computed
b3 = np.log(b2)*gamma
# # gamma-correction is performed
c = np.exp(b3)*255.0
# c is converted to type int
c1 = c.astype(int)
# c1 is converted from ndarray to image
im7 = scipy.misc.toimage(c1)
# displaying the image
subplot(2,4,8),imshow(im7),title('power law')
axis('off')


show()
