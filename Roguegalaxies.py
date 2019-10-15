from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from ClusterParams import abell1060 as bcg


# Open Image file, extract data and header
hdulist = fits.open('images/Abell1060_06554_03_wfpc2_f814w_pc_drz.fits')
# hdulist = fits.open('abell4059_wfpc2_f814w.fits')

hdu = hdulist[1]          # Holds image data
imagedata = hdu.data      # Extract the image data
hduheader = hdulist[0]    # Header that contains image details
mean = np.mean(imagedata)

np.set_printoptions(threshold=np.inf)
showstart = 'yes'
if showstart == 'yes':
    plt.figure()                        # Original, unaltered image:
    plt.title("Hubble ST Full Image")
    plt.imshow(imagedata, cmap='inferno', vmin=0, vmax=mean*40, origin={'lower', 'lower'})
    plt.colorbar()
    plt.show()

"""Global Parameters Used throughout the code"""
size = bcg[1]                                 # Half the width of the new image
iterations = np.linspace(0, size, bcg[8])
loops = len(iterations)
centre = [bcg[0][0], bcg[0][1]]               # Manually select the centre of image

angle = bcg[2]                  # Position angle
eccentricity = bcg[3]           # Eccentricity
imagecorrection = bcg[7][1]           # Corrects forimage ellipticity


def cutimage(initialcentre):
    """ Cuts Image down to size """

    a = initialcentre[0] - size
    b = initialcentre[0] + size
    c = initialcentre[1] - size
    d = initialcentre[1] + size

    datanew = imagedata[a:b, c:d]  # vertical, horizontal

    return datanew


"""Set up the image that needs to analysed"""
newdata = cutimage(centre)  # Now cut to area of image wanted for analysis

rotate = bcg[7][0]
if rotate == 'yes':
    newdata = np.rot90(newdata, k=1, axes=(0, 1))

# centrenew = centrefinal[0] + bcg[5][0], centrefinal[1] + bcg[5][1]   # Adjust for pixel offset
centrenew = bcg[1] - bcg[5][0], bcg[1] - bcg[5][1]


def intensity(imagearray):
    """A function that collects intensities into elliptical bins increasing linearly"""

    intensitylist = np.zeros(loops)
    insideimage = 2*int(size)
    rincrement = imagecorrection*size/loops  # Size each radius gets bigger by

    array = np.zeros((loops, (4*size**2)))
    array2 = np.zeros((loops, 4*size**2, 3))

    sinangle = np.sin(angle)
    cosangle = np.cos(angle)

    for i in range(insideimage):
        for j in range(insideimage):
            for k in range(loops):

                rmin = rincrement*k
                rmax = rincrement*k + rincrement

                theta = np.arctan((i - centrenew[0]) / (j - centrenew[1] + 0.0001)) - angle
                termone = ((j - centrenew[0]) * cosangle + (i - centrenew[1]) * sinangle) ** 2
                termtwo = ((j - centrenew[0]) * sinangle - (i - centrenew[1]) * cosangle) ** 2
                alpha = (termone + termtwo) ** 0.5

                r = alpha * (1 - (eccentricity**2)*(np.sin(theta))**2) ** 0.5

                if rmin <= r <= rmax:
                    array[k, i*j] = imagearray[i, j]
                    array2[k, i*j, 0] = imagearray[i, j]
                    array2[k, i*j, 1] = i
                    array2[k, i*j, 2] = j

    datasizehistory = np.zeros(loops)

    for l in range(loops):
        newlist = array[l, :][array[l, :] != 0]
        datasize = len(newlist)
        intensitylist[l] = sum(newlist) / datasize
        datasizehistory[l] = datasize

    return intensitylist, array, array2, datasizehistory


def imagemodel(p1, p2, p3, p4, p5):
    """Builds a model image"""

    I, rbreak, gamma, tau, beta = p1, p2, p3, p4, p5
    cosangle = np.cos(angle)
    sinangle = np.sin(angle)
    newarray = np.zeros((size*2, size*2))

    for i in range(size*2):
        for j in range(size*2):
            theta = np.arctan((i-centrenew[0])/(j-centrenew[1] + 0.000000000001)) - angle
            termone = ((j-centrenew[0])*cosangle + (i-centrenew[1])*sinangle)**2
            termtwo = ((j-centrenew[0])*sinangle - (i-centrenew[1])*cosangle)**2
            alpha = (termone + termtwo)**0.5

            r = alpha*(1 - (eccentricity**2)*(np.sin(theta))**2)**0.5

            newarray[i, j] = I*((r/rbreak)**(-gamma)) * (1 + (r/rbreak)**tau)**((gamma - beta)/tau)

    return newarray


# IMAGE DATA intensity information:
intensityinfo = intensity(newdata)[0]  # Intensity binning function working on the image data
modelimage = imagemodel(0.9, 40, -0.05, 1, 1.25)
modelintensity = intensity(modelimage)[0]


plt.figure(1)
plt.subplot(131)
plt.title("Cut Image Image")
plt.imshow(newdata, cmap='gray', vmin=0, vmax=mean * 40, origin={'lower', 'lower'})


plt.subplot(132)
plt.title("Model Image")
plt.imshow(modelimage, cmap='gray', vmin=0, vmax=mean * 40, origin={'lower', 'lower'})

plt.subplot(133)
plt.title("Subtracted Image")
plt.imshow(newdata - modelimage, cmap='gray', vmin=-1.0, vmax=mean * 40, origin={'lower', 'lower'})
# plt.colorbar()
plt.show()


plt.figure(2)
plt.subplot(211)

plt.plot(iterations, intensityinfo, marker='.', label='Model', color='black')
plt.plot(iterations, modelintensity, marker='.', label='Model', color='orange')
plt.xlabel('Radius')
plt.ylabel('Surface Brightness')
plt.yscale('log')
plt.xscale('log')
plt.subplot(212)
plt.plot(iterations, intensityinfo-modelintensity, 'g^')
plt.plot(iterations, np.zeros(len(iterations)))
plt.xscale('log')
plt.show()