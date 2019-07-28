from skimage import io
from skimage import feature
from skimage import color
from pylab import*
img = io.imread("./images/obama.png")
img = color.rgb2gray(img)
edge = feature.canny(img,3)
figure()
subplot(1, 2, 1), io.imshow(img), title("original Image")
subplot(1, 2, 2), io.imshow(edge), title("Canny")
show()

# import scipy.misc, numpy
# from skimage import feature
# from pylab import*
# from PIL import Image
# # opening the image and converting it to grayscale
# a = Image.open('./images/obama.png').convert('L')
# # converting a to an ndarray
# a = scipy.misc.fromimage(a)
# # performing Canny edge filter
# b = feature.canny(a,1)
# # b is converted from ndarray to an image
# #b = scipy.misc.toimage(b)
# # saving b as canny_output.png
# figure()
# subplot(1, 2, 1), imshow(a), title("original Image")
# subplot(1, 2, 2), imshow(b), title("Canny")
# show()
# #b.save('canny_output.png')
