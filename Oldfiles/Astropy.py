"""BCG Dust"""

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import pylab
from lmfit import Parameters, fit_report, Minimizer
from matplotlib.ticker import ScalarFormatter
import os
from matplotlib import font_manager as fm, rcParams


np.set_printoptions(threshold=np.inf)
showstart = 'yes'

# Open Image file, extract data and header
hdulist = fits.open('hst_08683_76_wfpc2_total_pc_drz.fits')
hdu = hdulist[1]          # Holds image data
imagedata = hdu.data      # Extract the image data
hduheader = hdulist[0]    # Header that contains image details
mean = np.mean(imagedata)

if showstart == 'yes':
    plt.figure()                        # Original, unaltered image:
    plt.title("Hubble ST Full Image")
    plt.imshow(imagedata, cmap='gray', vmin=0, vmax=mean*40, origin={'lower', 'lower'})
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


def cutimage(initialcentre):
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
parameters('yes')        # Image info if wanted

centre = [538, 440]         # Manually select the centre of image
size = 125                  # Half the size of the new image
newdata = cutimage(centre)  # Now cut to area of image wanted for analysis

# Find highest pixel in cut down image, return the pixel position:
centregalaxy = int(center(newdata)[0]), int(center(newdata)[1])
centrefinal = centregalaxy[0], centregalaxy[1]
centrenew = centrefinal[0] + 0.5, centrefinal[1] - 0.3   # Adjust for pixel offset


"""The Parameters of the Nuker Law and Ellipse Specification"""
centralintensity = 6.174
breakradius = 7.3189
gamma = -0.01351
tau = 1.596
beta = 1.8808

parameters = centralintensity, breakradius, gamma, tau, beta

# Ellipse settings of galaxy:
angle = np.pi / 2 + 0.23                   # Position angle
eccentricity = 0.64                        # Eccentricity


def intensity(imagearray):
    """A function that collects intensities into elliptical bins increasing linearly"""

    arrayinfo = imagearray
    intensitylist = np.zeros(len(iterations))
    insideimage = 2*int(size)
    rincrement = size/len(iterations)  # Size each radius gets bigger by

    array = np.zeros((len(iterations), 4*(size**2)))

    sinangle = np.sin(angle)
    cosangle = np.cos(angle)

    for i in range(insideimage):
        for j in range(insideimage):
            for k in range(len(iterations)):
                rmin = rincrement*k
                rmax = rincrement*k + rincrement

                theta = np.arctan((i - centrenew[0]) / (j - centrenew[1] + 0.0001)) - angle
                termone = ((j - centrenew[0]) * cosangle + (i - centrenew[1]) * sinangle) ** 2
                termtwo = ((j - centrenew[0]) * sinangle - (i - centrenew[1]) * cosangle) ** 2
                alpha = (termone + termtwo) ** 0.5

                r = alpha * (1 - (eccentricity**2)*(np.sin(theta))**2) ** 0.5

                if rmin <= r <= rmax:
                    array[k, i] = imagearray[i, j]

    datasizehistory = np.zeros(len(iterations))
    sxhistory = np.zeros(len(iterations))

    for l in range(len(iterations)):
        newlist = array[l, :][array[l, :] != 0]
        datasize = len(newlist)
        meannewlist = np.sum(newlist)/datasize

        mask = 'yes'
        if mask == 'yes' and np.sum(arrayinfo) != np.sum(modeldata):
            sx = standev(newlist, meannewlist, datasize)
            sxhistory[l] = sx
            listmasked = [i for i in newlist if -100*sx <= i <= 100*sx]
            newdatasize = len(listmasked)
            intensitylist[l] = sum(listmasked) / newdatasize
            datasizehistory[l] = newdatasize
        else:
            intensitylist[l] = sum(newlist) / datasize
            datasizehistory[l] = datasize

    return intensitylist, array, datasizehistory, sxhistory


def imagemodel(p1, p2, p3, p4, p5):
    """Builds a model image"""

    I = p1
    rbreak = p2
    gamma = p3
    tau = p4
    beta = p5

    cosangle = np.cos(angle)
    sinangle = np.sin(angle)
    newarray = np.zeros((size*2, size*2))

    for i in range(size*2):
        for j in range(size*2):
            theta = np.arctan((i-centrenew[0])/(j-centrenew[1] + 0.0001)) - angle
            termone = ((j-centrenew[0])*cosangle + (i-centrenew[1])*sinangle)**2
            termtwo = ((j-centrenew[0])*sinangle - (i-centrenew[1])*cosangle)**2
            alpha = (termone + termtwo)**0.5

            r = alpha*(1 - (eccentricity**2)*(np.sin(theta))**2)**0.5

            newarray[i, j] = I*((r/rbreak)**(-gamma)) * (1 + (r/rbreak)**tau)**((gamma - beta)/tau)

    return newarray


def newmodel(p1, p2, p3, p4, p5):
    """A model that is built from Nuker Law and returns a SB profile (not a model image)"""

    n = len(iterations)
    rinitial = size/n
    modelys = np.zeros(n)
    modelxs = np.linspace(rinitial/2, size, n)

    for i in range(n):
        r = modelxs[i]
        modelys[i] = p1 * ((r / p2)**(-p3)) * (1 + (r / p2)**p4)**((p3 - p5) / p4)

    return modelys, modelxs


def parametertesting(imagearray):
    """Testing one of the parameters at a time"""

    testingparameter = np.linspace(1.8, 2.0, 5)
    residualhistory = np.zeros(len(testingparameter))
    chi = np.zeros(len(iterations))

    parameterone = parameters[0]
    parametertwo = parameters[1]
    parameterthree = parameters[2]
    parameterfour = parameters[3]
    parameterfive = parameters[4]

    for i in range(len(testingparameter)):
        modelresults = imagemodel(parameterone, parametertwo, parameterthree, parameterfour, testingparameter[i])

        for t in range(len(iterations)):
            observed = intensity(imagearray)[0][t]
            expected = intensity(modelresults)[0][t]
            chi[t] = ((observed-expected)**2)/expected

        chisquared = np.sum(chi)
        residualhistory[i] = chisquared

    plt.figure()
    plt.title('I parameter testing')
    plt.plot(testingparameter, residualhistory)
    plt.show()

    return 1


def masking(imagearray, position):

    I = 6
    rbreak = 0.05
    gamma = 1
    tau = 1
    beta = 1

    starangle = np.pi/2
    stareccentricty = 0

    cosangle = np.cos(starangle)
    sinangle = np.sin(starangle)
    newarray = np.zeros((size*2, size*2))

    for i in range(size*2):
        for j in range(size * 2):
            theta = np.arctan((i - position[0]) / (j - position[1] + 0.0001)) - starangle
            termone = ((j - position[0]) * cosangle + (i - position[1]) * sinangle) ** 2
            termtwo = ((j - position[0]) * sinangle - (i - position[1]) * cosangle) ** 2
            alpha = (termone + termtwo) ** 0.5

            r = alpha * (1 - (stareccentricty ** 2) * (np.sin(theta)) ** 2) ** 0.5
            newarray[i, j] = I * ((r / rbreak) ** (-gamma)) * (1 + (r / rbreak) ** tau) ** ((gamma - beta) / tau)

    maskedimage = imagearray - newarray

    return maskedimage


"""Code that implements the main functions used to analyse images"""
testparameter = beta   # For the purpose of parameter testing only.

# Create a model of the BCG in question (Nuker Model), parameters inside function:
modeldata = imagemodel(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4])

# Find intensity of image and model data using the intenstity finding functions:
iterations = np.linspace(0, size, 150)

intensityinfo = intensity(newdata)  # Intensity binning function working on the image data
intensitydata = intensityinfo[0]    # The list of averaged intensities in each bin of image data
intensityarray = intensityinfo[1]   # The array containg all the bins (included for use in variance calculations)
binsize = intensityinfo[2]          # The binsize, used in the weighting of model fitting
imagestandev = intensityinfo[3]     # Standard deviation in bins, used for error bars and masking

modelinfo = intensity(modeldata)    # Intensity binning function working on the model data
intensitymodeldata = modelinfo[0]   # The list of averaged intensities in each bin of model data

# Create look at residuals in each elliptical bin:
chihistory = np.zeros(len(iterations))
for j in range(len(iterations)):
    chihistory[j] = (intensitydata[j] - intensitymodeldata[j])/intensitymodeldata[j]

print(chicalc(intensitydata, intensitymodeldata))
# parametertesting(newdata)


def plot(images, residuals, var, newmodeling):
    """A function that plots the wanted figures, this one is images, intensity & residual and variance graphs"""

    if images == 'yes':

        plt.figure(1)
        plt.subplot(131)
        plt.title("Cut Image Image")
        plt.imshow(newdata, cmap='gray', vmin=0, vmax=mean * 40, origin={'lower', 'lower'})
        # plt.plot(centrefinal[1], centrefinal[0], marker='x')
        # plt.axhline(y=60, color='r', linestyle='-')
        # plt.colorbar()

        plt.subplot(132)
        plt.title("Model Image")
        plt.imshow(modeldata, cmap='gray', vmin=0, vmax=mean * 40, origin={'lower', 'lower'})

        plt.subplot(133)
        plt.title("Subtracted Image")
        plt.imshow(newdata - modeldata, cmap='gray', vmin=-1.0, vmax=mean * 40, origin={'lower', 'lower'})
        # plt.colorbar()
        # plt.show()

    if residuals == 'yes':

        plt.figure(2)
        plt.subplot(211)
        # plt.plot(iterations, intensitydata, marker='x', label='Data')
        plt.plot(iterations, intensitymodeldata, marker='.', label='Model', color='black')
        plt.errorbar(iterations, intensitydata, yerr=imagestandev, marker='x', label='Data', color='green')

        pylab.legend(loc='upper right')
        plt.xlabel('Radius')
        plt.ylabel('Surface Brightness')
        # plt.yscale('log')
        plt.xscale('log')
        # ax = plt.axes(xscale='log', yscale='')
        # ax.get_yaxis().set_tick_params(which='both', direction='in')
        # ax.get_xaxis().set_tick_params(which='both', direction='in')
        # ax.yaxis.set_minor_locator(AutoMinorLocator(4))
        # ax2 = plt.twinx()
        # ax2.get_xaxis().set_tick_params(which='both', direction='in')
        # ax2.get_yaxis().set_tick_params(which='both', direction='in')
        # ax2.yaxis.set_minor_locator(AutoMinorLocator(4))
        # ax2.set_yticklabels([])
        # ax.tick_params(axis='both', which='minor', bottom='on', top="on")
        # plt.draw()

        plt.subplot(212)
        plt.plot(iterations, chihistory, 'g^')
        plt.plot(iterations, np.zeros(len(iterations)))
        plt.xscale('log')

        # plt.show()

    if var == 'yes':

        array = intensityarray
        bindata = np.zeros((3, len(iterations)))
        for l in range(len(iterations)):
            newlist = array[l, :][array[l, :] != 0]
            datasize = len(newlist)
            datamean = sum(newlist) / datasize
            variance = np.zeros(len(newlist))
            for i in range(len(newlist)):
                variance[i] = (newlist[i] - datamean) ** 2
            newvar = sum(variance)
            median = np.median(newlist)
            bindata[0, l] = datamean
            bindata[1, l] = newvar
            bindata[2, l] = median

        plt.figure(3)
        plt.plot(iterations, bindata[0], 'b')
        plt.plot(iterations, bindata[1], 'g')
        plt.plot(iterations, bindata[2], 'r')
        # plt.show()

    if newmodeling == 'yes':
        plt.figure(4)
        plt.subplot(211)
        xs = newmodel(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4])[1]
        ys = newmodel(parameters[0], parameters[1], parameters[2], parameters[3], parameters[4])[0]
        plt.plot(xs, ys, marker='.', label='Model')
        plt.plot(np.linspace(size/(2*len(iterations)), size, len(iterations)), intensitydata, marker='x', label='Data')
        pylab.legend(loc='upper right')
        plt.xlabel('Radius, r')
        plt.ylabel('Surface Brightness')
        plt.yscale('log')
        plt.xscale('log')
        plt.subplot(212)
        newresiduals = (ys - intensitydata)/ys
        plt.plot(xs, newresiduals, 'g^')
        plt.plot(iterations, np.zeros(len(iterations)))
        plt.xscale('log')

    plt.show()


def sbplotter(x, y, modely):

    xs = x
    ys = y
    ysmodel = modely
    xmin, xmax = 0.1, max(xs) + 3*max(xs)
    ymin, ymax = min(ys) - 0.05*min(ys), max(ys) + 0.05*max(ys)

    fpath = os.path.join(rcParams["datapath"], "fonts/ttf/nimbusmono-bold.ttf")
    prop = fm.FontProperties(fname=fpath)
    fname = os.path.split(fpath)[1]
    print(prop)

    fig = plt.figure()
    ax1 = fig.add_axes([0.15, 0.3, 0.7, 0.6])
    ax1.set_xscale("log")
    ax1.plot(xs, ys, marker='s', color='black', ms=3)
    ax1.plot(xs, ysmodel)
    ax1.axis([xmin, xmax, ymax, ymin])
    # ax1.set_yscale("log")
    ax1.get_yaxis().set_tick_params(which='both', direction='in')
    ax1.get_xaxis().set_tick_params(which='both', direction='in')
    ax1.tick_params(axis='both', which='both', top='True', right='True')
    ax1.tick_params(labelbottom=False)
    ax1.set_yticklabels(ax1.get_yticks(), fontproperties=prop, size=12)
    ax1.set_ylabel('M', fontproperties=prop, color='black', rotation=0, labelpad=28, size=13)
    # ax1.set_title('Surface Brightness Profile', fontproperties=prop, color='black', size=12)

    ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.2])
    ax2.semilogx(xs, ysmodel - ys)                   # Must be the same as in axes 3
    ax2.axis([xmin, xmax, -0.2, 0.2])
    ticks = 0.1, 0, -0.1
    ax2.set_yticks(ticks, minor=False)
    ax2.get_yaxis().set_tick_params(which='both', direction='in')
    ax2.get_xaxis().set_tick_params(which='both', direction='in')
    ax2.tick_params(axis='both', which='both', top='True', right='True')
    ax2.set_xlabel('R [arcseconds]', fontproperties=prop, color='black', size=12)
    ax2.set_xticklabels(ax2.get_xticks(), fontproperties=prop, size=12)
    ax2.set_yticklabels(ax2.get_yticks(), fontproperties=prop, size=11)
    ax2.set_ylabel('$\Delta$M', fontproperties=prop, color='black', rotation=0, labelpad=16, size=12)

    ax3 = fig.add_axes((0.15, 0.2, 0.7, 0.1))
    ax3.yaxis.set_visible(False)
    ax3.get_xaxis().set_tick_params(which='both', direction='inout')
    ax3.tick_params(labelbottom=False)
    ax3.set_xscale("log")
    ax3.axis([xmin, xmax, 0, 0.1])
    ax3.set_xlim(ax1.get_xlim()[0], ax1.get_xlim()[1])
    ax3.spines['bottom'].set_position('zero')
    ax3.patch.set_alpha(0)

    for axis in [ax1.xaxis, ax1.yaxis]:
        axis.set_major_formatter(ScalarFormatter())
    for axis in [ax2.xaxis, ax2.yaxis]:
        axis.set_major_formatter(ScalarFormatter())

    plt.show()

    return 1


def coordsconverter(ys):

    photzpt = hdu.header['PHOTZPT']
    flux = (ys*hdu.header['photflam'])/hduheader.header['exptime']
    magnitude = -2.5*np.log10(flux) + photzpt

    n = len(iterations)
    rinitial = size/n
    initialxs = np.linspace(rinitial/2, size, n)
    arcsecperpixel = 3.17
    radius = initialxs

    return radius, magnitude


def residual(params):

    v = params.valuesdict()
    ci = v['ci']
    br = v['br']
    g = v['g']
    t = v['t']
    b = v['b']

    # res = intensitydata - intensity(imagemodel(ci, br, g, t, b))[0]
    res = (intensitydata - newmodel(ci, br, g, t, b)[0])/np.sqrt(binsize*intensitydata)

    return res


# Decide what to plot (images, intensities, variance):
plot('yes', 'no', 'no', 'no')

"""The parameter fitting section of the code"""
fitparameters = 'yes'
if fitparameters == 'yes':
    params = Parameters()
    params.add('ci', value=parameters[0])
    params.add('br', value=parameters[1])
    params.add('g', value=parameters[2])
    params.add('t', value=parameters[3])
    params.add('b', value=parameters[4])
    mini = Minimizer(residual, params, fcn_args=())
    out = mini.minimize()
    print(fit_report(out))
    ci = out.params['ci'].value
    br = out.params['br'].value
    g = out.params['g'].value
    t = out.params['t'].value
    b = out.params['b'].value
    print(ci, br, g, t, b)


# plt.figure()
# starone = 223, 152
# mask = masking(newdata, starone)
# plt.imshow(mask, cmap='gray', vmin=0, vmax=mean*40, origin={'lower', 'lower'})
# plt.colorbar()
# plt.show()

rarcsecs = coordsconverter(intensitydata)[0]
m = coordsconverter(intensitydata)[1]
modelm = coordsconverter(intensitymodeldata)[1]
sbplotter(rarcsecs, m, modelm)

# fig, ax = plt.subplots()
# X, Y = np.meshgrid(newdata[0, :], newdata[:, 0])
# ax.contour(X, Y, newdata)
# plt.show()
