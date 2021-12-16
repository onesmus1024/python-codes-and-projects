import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread("/media/onesmus/dev/dev/python/matplotlib/donut_circle.png")
print(img)
img = img[:, :, 0]
imgplot = plt.imshow(img,cmap="hot")
imgplot.set_cmap('nipy_spectral')
print(img)
plt.colorbar()
plt.show()