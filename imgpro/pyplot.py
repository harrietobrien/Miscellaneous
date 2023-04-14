from skimage import io, exposure
import matplotlib.pyplot as plt
from skimage.util import img_as_ubyte

image = io.imread('sandpack_16bit.tif')
plt.hist(image.ravel(), bins=65536, range=(34000, 36000))
plt.xlabel('Intensity Value')
plt.ylabel('Count')
plt.show()
image_rescale = exposure.rescale_intensity(image, out_range=(0, 2**31 - 1))
img_uint8 = img_as_ubyte(image_rescale)
image = exposure.rescale_intensity(image, in_range=(34000, 36000))
io.imsave('new_image.tif', image)