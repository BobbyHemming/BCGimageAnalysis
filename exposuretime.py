from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from ClusterParams import abell160 as bcg
from ClusterParams import abell3144 as bcg1
from ClusterParams import abell1060 as bcg2
from ClusterParams import abell3716 as bcg4
from ClusterParams import abell4059 as bcg5


np.set_printoptions(threshold=np.inf)
showstart = 'yes'

# Open Image file, extract data and header
hdulist = fits.open('images/abell160_wfpc2_f814w.fits')
hdu = hdulist[1]          # Holds image data
imagedata = hdu.data      # Extract the image data
hduheader = hdulist[0]    # Header that contains image details
mean = np.mean(imagedata)
exptime = hduheader.header['exptime']


# Open Image file, extract data and header
hdulist1 = fits.open('images/abell3144_wfpc2_total.fits')
hdu1 = hdulist1[1]          # Holds image data
imagedata1 = hdu1.data      # Extract the image data
hduheader1 = hdulist1[0]    # Header that contains image details
mean1 = np.mean(imagedata)

# Open Image file, extract data and header
hdulist2 = fits.open('images/Abell1060_06554_03_wfpc2_f814w_pc_drz.fits')
hdu2 = hdulist2[1]          # Holds image data
imagedata2 = hdu2.data      # Extract the image data
hduheader2 = hdulist2[0]    # Header that contains image details
mean2 = np.mean(imagedata)

# Open Image file, extract data and header
hdulist4 = fits.open('images/abell3716_PC_f814w.fits')
hdu4 = hdulist4[1]          # Holds image data
imagedata4 = hdu4.data      # Extract the image data
hduheader4 = hdulist4[0]    # Header that contains image details
mean4 = np.mean(imagedata)

# Open Image file, extract data and header
hdulist5 = fits.open('images/abell4059_wfpc2_f814w.fits')
hdu5 = hdulist5[1]          # Holds image data
imagedata5 = hdu5.data      # Extract the image data
hduheader5 = hdulist5[0]    # Header that contains image details
mean5 = np.mean(imagedata)


if showstart == 'yes':
    plt.figure()                        # Original, unaltered image:
    plt.title("Hubble ST Full Image")
    plt.imshow(imagedata, cmap='inferno', vmin=0, vmax=mean*40, origin={'lower', 'lower'})
    plt.colorbar()
    plt.show()


def parameters(yesorno):
    """ A Function that holds all the telescope information, will print if wanted"""

    # Extract the details of image from header:
    dimensions = hdu.header['NAXIS1'], hdu.header['NAXIS2']  # Image dimensions (no. pixel width, no. pixel height)
    date = hduheader.header['DATE']  # Date image was taken
    telescope = hduheader.header['TELESCOP']  # Telescope used to take image
    RA = hdu.header['CRVAL1']  # Right ascension
    DEC = hdu.header['CRVAL2']  # Declination

    photflam = hdu.header['photflam']
    exptime = hduheader.header['exptime']
    data = imagedata * photflam / exptime
    mean = np.mean(imagedata)               # The mean value of pixels in the image

    if yesorno == 'yes':
        # Print them for inspection:
        hdulist.info()
        print(hdu.header)
        print(date)
        print(telescope)
        print(dimensions)

        # Co-ords of reference pixel; RA (deg), DEC (deg)
        print('[ RA (deg):', RA, ', DEC (deg):', DEC, ']')


def center(imagearray):
    """Highest Intensity Pixel found"""

    maxvalue = np.amax(imagearray)
    maxindex = np.where(imagearray == maxvalue)
    maxindex1 = maxindex[0]
    maxindex2 = maxindex[1]

    return maxindex1, maxindex2, maxvalue


def cutimage(initialcentre, imagedata):
    """ Cuts Image down to size """

    a = initialcentre[0] - size
    b = initialcentre[0] + size
    c = initialcentre[1] - size
    d = initialcentre[1] + size

    datanew = imagedata[a:b, c:d]  # vertical, horizontal

    return datanew


def standev(xi, xbar, n):
    """Standad deviation Calculator"""
    sx = np.sqrt(np.sum((xi - xbar)**2)/(n-1))
    return sx


def chicalc(xi, mi):
    """Chi Squared calculator"""
    chisq = np.sum(((xi - mi)**2)/mi)
    return chisq


"""Set up the image that needs to analysed"""
parameters('no')        # Image info if wanted

centre = [bcg[0][0], bcg[0][1]]         # Manually select the centre of image
size = 80                 # Half the size of the new image
newdata = cutimage(centre, imagedata)  # Now cut to area of image wanted for analysis

centre1 = [bcg1[0][0], bcg1[0][1]]         # Manually select the centre of image
size1 = 50                  # Half the size of the new image
newdata1 = cutimage(centre1, imagedata1)  # Now cut to area of image wanted for analysis

centre2 = [bcg2[0][0], bcg2[0][1]]         # Manually select the centre of image
size2 = 100                  # Half the size of the new image
newdata2 = cutimage(centre2, imagedata2)  # Now cut to area of image wanted for analysis

centre4 = [bcg4[0][0], bcg4[0][1]]         # Manually select the centre of image
size4 = 50                  # Half the size of the new image
newdata4 = cutimage(centre4, imagedata4)  # Now cut to area of image wanted for analysis

centre5 = [bcg5[0][0], bcg5[0][1]]         # Manually select the centre of image
size5 = 50                  # Half the size of the new image
newdata5 = cutimage(centre5, imagedata5)  # Now cut to area of image wanted for analysis


plt.figure()                        # Original, unaltered image:
plt.imshow(newdata, cmap='gray', vmin=0, vmax=mean*100, origin={'lower', 'lower'})
plt.colorbar()
plt.show()

plt.figure()                        # Original, unaltered image:
plt.imshow(newdata1, cmap='gray', vmin=0, vmax=mean1*120, origin={'lower', 'lower'})
plt.colorbar()
plt.show()

plt.figure()                        # Original, unaltered image:
plt.imshow(newdata2, cmap='gray', vmin=0, vmax=mean2*100, origin={'lower', 'lower'})
plt.colorbar()
plt.show()

plt.figure()                        # Original, unaltered image:
plt.imshow(newdata4, cmap='gray', vmin=0, vmax=mean4*80, origin={'lower', 'lower'})
plt.colorbar()
plt.show()

plt.figure()                        # Original, unaltered image:
plt.imshow(newdata5, cmap='gray', vmin=0, vmax=mean5*120, origin={'lower', 'lower'})
plt.colorbar()
plt.show()



