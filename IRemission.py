from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import cv2

image = open("imageDownload-11-irsawebops8---1.png")


image = cv2.imread("imageDownload-11-irsawebops8---1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
mean = np.mean(gray)
#
# # Open Image file, extract data and header
# hdulist = fits.open('WISE-Band-4.fits')
#
# hdu = hdulist[0]          # Holds image data
# imagedata = hdu.data      # Extract the image data
# hduheader = hdulist[0]    # Header that contains image details
# mean = np.mean(imagedata)
#
# print(hduheader)
#
np.set_printoptions(threshold=np.inf)
showstart = 'yes'
if showstart == 'yes':
    plt.figure()                        # Original, unaltered image:
    plt.title("Hubble ST Full Image")
    plt.imshow(gray, cmap='binary', vmin=0, vmax=mean*10, origin={'lower', 'lower'})
    plt.colorbar()
    plt.show()





