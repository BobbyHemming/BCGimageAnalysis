"""BCG Dust"""

from astropy.io import fits
import numpy as np
import pylab
import os
import matplotlib.pyplot as plt
from lmfit import Parameters, fit_report, Minimizer
from matplotlib.ticker import ScalarFormatter
from matplotlib import font_manager as fm, rcParams
from numpy import diff
from ClusterParams import abell4059 as bcg

# Open Image file, extract data and header
hdulist = fits.open('abell4059_wfpc2_f814w.fits')

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
parameters('no')        # Image info if wanted
newdata = cutimage(centre)  # Now cut to area of image wanted for analysis

rotate = bcg[7][0]
if rotate == 'yes':
    newdata = np.rot90(newdata, k=1, axes=(0, 1))

# Find highest pixel in cut down image, return the pixel position:
centregalaxy = int(center(newdata)[0]), int(center(newdata)[1])
centrefinal = centregalaxy[0], centregalaxy[1]
centrenew = centrefinal[0] + bcg[5][0], centrefinal[1] + bcg[5][1]   # Adjust for pixel offset


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
    sxhistory = np.zeros(loops)

    for l in range(loops):
        newlist = array[l, :][array[l, :] != 0]
        datasize = len(newlist)
        intensitylist[l] = sum(newlist) / datasize
        datasizehistory[l] = datasize

    return intensitylist, array, datasizehistory, sxhistory, array2


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


def newmodel(p1, p2, p3, p4, p5):
    """A model that is built from Nuker Law and returns a SB profile (not a model image)"""

    n = loops
    rinitial = imagecorrection*size/n
    modelys = np.zeros(n)
    modelxs = np.linspace(rinitial/2, imagecorrection*size, n)

    for i in range(n):
        r = modelxs[i]
        modelys[i] = p1 * ((r / p2)**(-p3)) * (1 + (r / p2)**p4)**((p3 - p5) / p4)

    return modelys, modelxs


def residual(params):

    v = params.valuesdict()
    ci, br, g, t, b = v['ci'], v['br'], v['g'], v['t'], v['b']
    # res = intensitydata - intensity(imagemodel(ci, br, g, t, b))[0]
    res = (intensitydata - newmodel(ci, br, g, t, b)[0])/np.sqrt(binsize*intensitydata)

    return res


# IMAGE DATA intensity information:
intensityinfo = intensity(newdata)  # Intensity binning function working on the image data
intensitydata = intensityinfo[0]    # The list of averaged intensities in each bin of image data
intensityarray = intensityinfo[1]   # The array containg all the bins (included for use in variance calculations)
binsize = intensityinfo[2]          # The binsize, used in the weighting of model fitting
imagestandev = intensityinfo[3]     # Standard deviation in bins, used for error bars and masking
holdingarray = intensityinfo[4]


"""The parameter fitting section of the code"""
params = Parameters()
params.add('ci', value=bcg[4][0])
params.add('br', value=bcg[4][1])
params.add('g', value=bcg[4][2])
params.add('t', value=bcg[4][3])
params.add('b', value=bcg[4][4])
mini = Minimizer(residual, params, fcn_args=())
out = mini.minimize()
ci = out.params['ci'].value
br = out.params['br'].value
g = out.params['g'].value
t = out.params['t'].value
b = out.params['b'].value
clusterparams = ci, br, g, t, b

printfittingreport = 'yes'
if printfittingreport == 'yes':
    print(fit_report(out))
    print(ci, br, g, t, b)


# Create a model of the BCG in question (Nuker Model), parameters inside function:
modeldata = imagemodel(ci, br, g, t, b)
modelinfo = intensity(modeldata)    # Intensity binning function working on the model data
intensitymodeldata = modelinfo[0]   # The list of averaged intensities in each bin of model data


def sbplotter(x, y, modely):

    xs, ys = x, y
    ysmodel = modely
    xmin, xmax = 0, max(xs) + 2*max(xs)
    ymin, ymax = min(ys) - 0.05*min(ys), max(ys) + 0.05*max(ys)

    fpath = os.path.join(rcParams["datapath"], "fonts/ttf/nimbusmono-bold.ttf")
    prop = fm.FontProperties(fname=fpath)
    fname = os.path.split(fpath)[1]
    print(prop)

    fig = plt.figure()
    ax1 = fig.add_axes([0.15, 0.3, 0.7, 0.6])
    ax1.set_xscale("log")
    ax1.plot(xs, ys, marker='s', color='black', ms=3)
    ax1.plot(xs, maskedm, color='orange')
    ax1.plot(xs, ysmodel)

    plt.text(0.05*xmax, ymin + 1, 'ESO 325-G16', fontproperties=prop, size=15)
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
    ax2.semilogx(xs, ysmodel - maskedm, color='orange')  # Must be the same as in axes 3
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

    n = loops
    rinitial = size/n
    initialxs = np.linspace(rinitial/2, size, n)
    arcsecperpixel = 0.05
    radius = initialxs*arcsecperpixel

    return radius, magnitude


def masker2(arraytobestripped):

    insideimage = 2*int(size)
    intensityhistory = np.zeros(loops)
    array = arraytobestripped
    maskedimage = np.zeros((insideimage, insideimage))

    for l in range(loops):

        strippedarray = array[l, :, :][array[l, :, 0] != 0]
        meanlist = np.sum(strippedarray[:, 0])/len(strippedarray[:, 0])
        sx = standev(strippedarray[:, 0], meanlist, len(strippedarray[:, :]))
        newbin = []

        for t in range(len(strippedarray[:, 0])):
            i = int(strippedarray[t, 1])
            j = int(strippedarray[t, 2])
            if -3*sx + meanlist <= strippedarray[t, 0] <= 3*sx + meanlist:
                maskedimage[i, j] = 0
                newbin.append(strippedarray[t, 0])
            else:
                # strippedarray[t, 0] = meanlist
                # np.delete(strippedarray, [t, 0])
                maskedimage[i, j] = 1

        # intensityhistory[l] = np.sum(strippedarray[:, 0])/len(strippedarray[:, 0])
        intensityhistory[l] = np.sum(newbin)/len(newbin)

    return intensityhistory, maskedimage


def dustfinder(arraytobestripped):

    insideimage = 2 * int(size)
    intensityhistory = np.zeros(loops)
    array = arraytobestripped
    maskedimage = np.zeros((insideimage, insideimage))
    binsizehistory = np.zeros(loops)

    for l in range(loops):

        strippedarray = array[l, :, :][array[l, :, 0] != 0]
        meanlist = np.sum(strippedarray[:, 0]) / len(strippedarray[:, 0])
        sx = standev(strippedarray[:, 0], meanlist, len(strippedarray[:, :]))
        newbin = []

        for t in range(len(strippedarray[:, 0])):
            i = int(strippedarray[t, 1])
            j = int(strippedarray[t, 2])
            if 0.9*meanlist <= strippedarray[t, 0] <= 3*sx + meanlist:
                maskedimage[i, j] = 0
                newbin.append(strippedarray[t, 0])
            else:
                maskedimage[i, j] = 1

        binsizehistory[l] = len(newbin)
        intensityhistory[l] = np.sum(newbin) / len(newbin)

    return intensityhistory, maskedimage, binsizehistory


rarcsecs = coordsconverter(intensitydata)[0]
m = coordsconverter(intensitydata)[1]
modelm = coordsconverter(intensitymodeldata)[1]
maskedm = coordsconverter(masker2(holdingarray)[0])[1]
dustmodifiedm = coordsconverter(dustfinder(holdingarray)[0])[1]
rawdustmodifiedm = dustfinder(holdingarray)[0]

sbplotter(rarcsecs, m, modelm)
sbplotter(rarcsecs, m, dustmodifiedm)


def plot(images, residuals, var, newmodeling, extinction):
    """A function that plots the wanted figures, this one is images, intensity & residual and variance graphs"""

    if images == 'yes':
        meannew = np.mean(newdata)
        greyscalesetting = bcg[6]
        plt.figure(1)
        plt.subplot(131)
        plt.title("Cut Image Image")
        plt.imshow(newdata, cmap='gray', vmin=-1.0, vmax=meannew * greyscalesetting, origin={'lower', 'lower'})
        # plt.plot(centrefinal[1], centrefinal[0], marker='x')
        # plt.axhline(y=60, color='r', linestyle='-')
        # plt.colorbar()

        plt.subplot(132)
        plt.title("Model Image")
        plt.imshow(modeldata, cmap='gray', vmin=-1.0, vmax=meannew * greyscalesetting, origin={'lower', 'lower'})

        plt.subplot(133)
        plt.title("Subtracted Image")
        plt.imshow(newdata - modeldata, cmap='gray', vmin=-1.0, vmax=meannew * greyscalesetting,
                   origin={'lower', 'lower'})
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
        plt.plot(np.linspace(size / (2 * len(iterations)), size, len(iterations)), intensitydata, marker='x',
                 label='Data')
        pylab.legend(loc='upper right')
        plt.xlabel('Radius, r')
        plt.ylabel('Surface Brightness')
        plt.yscale('log')
        plt.xscale('log')
        plt.subplot(212)
        newresiduals = (ys - intensitydata) / ys
        plt.plot(xs, newresiduals, 'g^')
        plt.plot(iterations, np.zeros(len(iterations)))
        plt.xscale('log')

    if extinction == 'yes':
        plt.figure()
        plt.imshow(newdata / modeldata, cmap='inferno', vmin=0, vmax=mean * 40, origin={'lower', 'lower'})
        plt.colorbar()
        plt.show()

    plt.show()


def parametertesting(imagearray, params):
    """Testing one of the parameters at a time"""

    testingparameter = np.linspace(1.8, 2.0, 5)
    residualhistory = np.zeros(len(testingparameter))
    chi = np.zeros(loops)

    parameterone = params[0]
    parametertwo = params[1]
    parameterthree = params[2]
    parameterfour = params[3]
    parameterfive = params[4]

    for i in range(len(testingparameter)):
        modelresults = imagemodel(parameterone, parametertwo, parameterthree, parameterfour, testingparameter[i])

        for t in range(loops):
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


def deriv(xs, ys):
    dx = xs[1] - xs[0]
    dydx = np.gradient(ys, dx)

    return dydx


# Decide what to plot (images, intensities, variance):
plot('yes', 'no', 'no', 'no', 'yes')

plt.figure()
plt.imshow(masker2(holdingarray)[1], cmap='inferno', vmin=0, vmax=mean * 80, origin={'lower', 'lower'})
plt.colorbar()
plt.show()

plt.figure()
plt.imshow(dustfinder(holdingarray)[1], cmap='inferno', vmin=0, vmax=mean * 80, origin={'lower', 'lower'})
plt.colorbar()
plt.show()

newbinsize = dustfinder(holdingarray)[2]

np.savetxt("A4059.txt", (rarcsecs, m, modelm, dustmodifiedm, rawdustmodifiedm), fmt="%f")

plt.figure()
plt.plot()
