from PIL import Image
from pylab import *

im = Image.open("./images/obama.png")
im2 =im.convert('L')
figure()
subplot(1,2,1) ,imshow(im),title("anh goc")
axis('off')
subplot(1,2,2) ,imshow(im2),title("Anh xam")
axis('off')
show()
im.save('obama2.png')