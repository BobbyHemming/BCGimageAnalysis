"""BCG Dust"""

from astropy.io import fits
import numpy as np
import os
import matplotlib.pyplot as plt
from lmfit import Parameters, fit_report, Minimizer
from matplotlib.ticker import ScalarFormatter
from matplotlib import font_manager as fm, rcParams
from numpy import diff
from ClusterParams import abell4059 as bcg
abell = 4059
# Open Image file, extract data and header
hdulist = fits.open(bcg[11])

# This is the master branch.
# TODO: make a galaxy class so galaxies can be stored as objects rather than difficult lists of items

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


def deriv(xs, ys):

    derivs = diff(ys)/diff(xs)

    return derivs


"""Set up the image that needs to analysed"""
parameters('no')        # Image info if wanted
newdata = cutimage(centre)  # Now cut to area of image wanted for analysis

rotate = bcg[7][0]
if rotate == 'yes':
    newdata = np.rot90(newdata, k=1, axes=(0, 1))


# Find highest pixel in cut down image, return the pixel position:
centregalaxy = int(center(newdata)[0]), int(center(newdata)[1])
centrefinal = centregalaxy[0], centregalaxy[1]
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
holdingarray = intensityinfo[2]     # Holding array with positions of particles in as well
binsize = intensityinfo[3]

np.seterr(all='raise')

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


plt.figure()
plt.imshow(newdata, cmap='gray', vmin=0, vmax=np.mean(newdata)*bcg[6], origin={'lower', 'lower'})
plt.colorbar()
plt.show()

plt.figure()
plt.imshow(modeldata, cmap='gray', vmin=0, vmax=np.mean(modeldata)*bcg[6], origin={'lower', 'lower'})
plt.colorbar()
plt.show()

plt.figure()
plt.imshow(newdata - modeldata, cmap='gray', vmin=0, vmax=np.mean(modeldata)*bcg[6]*0.7, origin={'lower', 'lower'})
plt.colorbar()
plt.show()

# filename1 = "A{}image.txt".format(abell)
# image = newdata - modeldata
# np.savetxt(filename1, image, fmt="%f")


def sbplotter(x, y, modely, dustmodified):

    xs, ys = x, y
    ysmodel = modely
    dustmod = dustmodified

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
    ax1.plot(xs, dustmod, color='orange')
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
    ax2.semilogx(xs, dustmod - ys, color='orange')  # Must be the same as in axes 3
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
        print(sx)
        newbin = []

        for t in range(len(strippedarray[:, 0])):
            i = int(strippedarray[t, 1])
            j = int(strippedarray[t, 2])
            if 0.9*meanlist <= strippedarray[t, 0] <= 3*sx + meanlist:
                maskedimage[i, j] = 0
                newbin.append(strippedarray[t, 0])
            else:
                maskedimage[i, j] = 0

            if strippedarray[t, 0] >= 3*sx + meanlist:
                maskedimage[i, j] = strippedarray[t, 0]

        binsizehistory[l] = len(newbin)
        intensityhistory[l] = np.sum(newbin) / len(newbin)

    return intensityhistory, maskedimage, binsizehistory


# The Data for a BCG with no dust in (Dust and bright sources have been masked):
rawdustmodifiedm = dustfinder(holdingarray)[0]  # Co-ors have not been converted yet
newbinsize = dustfinder(holdingarray)[2]

# Data with co-ords converted:
rarcsecs = coordsconverter(intensitydata)[0]
m = coordsconverter(intensitydata)[1]
modelm = coordsconverter(intensitymodeldata)[1]
dustmodifiedm = coordsconverter(rawdustmodifiedm)[1]


sbplotter(rarcsecs, m, modelm, dustmodifiedm)


def newresidual(params):

    v = params.valuesdict()
    ci, br, g, t, b = v['newci'], v['newbr'], v['newg'], v['newt'], v['newb']
    # res = intensitydata - intensity(imagemodel(ci, br, g, t, b))[0]
    res = (rawdustmodifiedm - newmodel(ci, br, g, t, b)[0])/np.sqrt(newbinsize*rawdustmodifiedm)

    return res


# """The parameter fitting section of the code"""
newparams = Parameters()
# newparams.add('newci', value=ci)
# newparams.add('newbr', value=br)
# newparams.add('newg', value=g)
# newparams.add('newt', value=t)
# newparams.add('newb', value=b)
newparams.add('newci', value=bcg[4][0])
newparams.add('newbr', value=bcg[4][1])
newparams.add('newg', value=bcg[4][2])
newparams.add('newt', value=bcg[4][3])
newparams.add('newb', value=bcg[4][4])

newmini = Minimizer(newresidual, newparams, fcn_args=())
newout = newmini.minimize()
newci = newout.params['newci'].value
newbr = newout.params['newbr'].value
newg = newout.params['newg'].value
newt = newout.params['newt'].value
newb = newout.params['newb'].value
newclusterparams = newci, newbr, newg, newt, newb

printfittingreport = 'no'
if printfittingreport == 'yes':
    print(fit_report(newout))
    print(newci, newbr, newg, newt, newb)

nodustmodelimage = imagemodel(newci, newbr, newg, newt, newb)
extinctionimage = -2.5*np.log10(abs(newdata/nodustmodelimage))
nodustmodelsbp = coordsconverter(intensity(nodustmodelimage)[0])[1]


def imageplotter(imageone, imagetwo):

    plt.figure()
    plt.imshow(imagetwo, cmap='inferno', vmin=-0.3, vmax=mean*80, origin={'lower', 'lower'})
    plt.colorbar()
    plt.show()

    plt.figure()
    plt.imshow(imageone, cmap='inferno', vmin=0, vmax=mean * 80, origin={'lower', 'lower'})
    plt.colorbar()
    plt.show()

    plt.figure()
    plt.imshow(imageone - imagetwo, cmap='binary', vmin=0, vmax=mean * 13, origin={'lower', 'lower'})
    plt.colorbar()
    plt.show()

    return 1


def extinctionfinder(image):

    protonmass = 1.6726219*10**(-27)  # Mass of proton in kg
    sunmass = 1.98847*10**30          # Mass of the sun in kg
    columndensity = 1.81*10**21       # dust column density

    pixeldustlist = []

    totalradius = 20                       # In P
    D = bcg[9]                           # In Mpc

    # tenkpcradius = int(0.01/(D)*(180/np.pi)*3600)
    # totalradius = tenkpcradius
    distance = D*(3.0856776*10**18)*10**6  # In cm so can use in dust conversion
    convertedradius = (totalradius*(0.05*np.pi)/(3600*180))*distance

    newimage = convertedradius * image / totalradius

    for i in range(size*2):
        for j in range(size*2):
            r = np.sqrt((i - centrenew[0])**2 + (j - centrenew[1])**2)
            if r < totalradius and 0.1 <= image[i, j] <= 0.8:
                dustmass = protonmass*columndensity*image[i, j]*(convertedradius/totalradius)**2/sunmass
                newimage[i, j] = dustmass
                pixeldustlist.append(dustmass)
            else:
                newimage[i, j] = 0

    newdust = np.sum(pixeldustlist)

    return newimage, newdust


imageplotter(nodustmodelimage, newdata)
# imageplotter(newdata, modeldata)
# imageplotter(extinctionimage, newdata)
dustmass = extinctionfinder(extinctionimage)[1]

print('Dust mass is =', dustmass)
filename = "datafiles/A{}.txt".format(abell)
np.savetxt(filename, (rarcsecs, m, modelm, dustmodifiedm, nodustmodelsbp), fmt="%f")

# tbs = abell, dustmass
# with open('datafiles/dustlist.txt', "a") as text_file:
#     text_file.write(str(tbs) + '\n')


plt.figure()
plt.imshow(extinctionfinder(extinctionimage)[0], cmap='gray', vmin=0, vmax=np.amax(extinctionfinder(extinctionimage)[0]), origin={'lower', 'lower'})
plt.colorbar()
plt.show()

plt.figure()
plt.imshow(1 - newdata/nodustmodelimage, cmap='binary', vmin=0, vmax=np.mean(1 - newdata/nodustmodelimage)*3, origin={'lower', 'lower'})
plt.colorbar()
plt.show()


newextinction = 1 - newdata/nodustmodelimage

