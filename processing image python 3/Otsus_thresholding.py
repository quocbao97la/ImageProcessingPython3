import matplotlib.pyplot as plt
from skimage import data
from skimage import filters
from skimage import exposure
from PIL import Image
import os
import cv2
import sys
import numpy as np
from PIL import Image

path_png = "./images/obama.png"
path_jpg = "0002.jpg"

image = np.asarray((Image.open(path_png)).convert('L'))

#camera = data.camera()
# camera = Image.open("input.png")
# print(camera.size)
#
#
val = filters.threshold_otsu(image)
hist, bins_center = exposure.histogram(image)
#
plt.figure(figsize=(9, 4))
plt.subplot(131)
plt.imshow(image, cmap='gray')
plt.subplot(132)
a = image < val
plt.imshow(a, cmap='gray')
plt.axis('off')
plt.subplot(133)
plt.plot(bins_center, hist, lw=2)
plt.axvline(val, color='k', ls='--')


plt.show()