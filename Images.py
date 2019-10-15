from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from ClusterParams import abell3144 as BCG
import matplotlib as mpl
from matplotlib import font_manager as fm, rcParams
from ClusterParams import galaxylist as glist
import matplotlib.gridspec as gridspec
abell = 3144

centres = glist[0][0], glist[1][0], glist[2][0], glist[3][0], glist[4][0], glist[5][0], glist[6][0], glist[7][0], \
          glist[8][0], glist[9][0], glist[10][0], glist[11][0]

hdulist76 = fits.open('images/Abell1795_04_wfpc2_f555w_pc_drz.fits')
imagedata76 = hdulist76[1].data

hdulist119 = fits.open('images/abell119_wfpc2_pc.fits')
imagedata119 = hdulist119[1].data

hdulist147 = fits.open('images/abell147_wfpc2_pc.fits')
imagedata147 = hdulist147[1].data

hdulist160 = fits.open('images/abell160_wfpc2_f814w.fits')
imagedata160 = hdulist160[1].data

hdulist168 = fits.open('images/abell168_wfpc2_pc.fits')
imagedata168 = hdulist168[1].data

hdulist189 = fits.open('images/abell189_wfpc2_pc.fits')
imagedata189 = hdulist189[1].data

hdulist193 = fits.open('images/abell193_wfpc2_pc.fits')
imagedata193 = hdulist193[1].data

hdulist195 = fits.open('images/Abell195_08683_09_wfpc2_f814w_pc_drz.fits')
imagedata195 = hdulist195[1].data

hdulist260 = fits.open('images/Abell260_08683_10_wfpc2_f814w_pc_drz.fits')
imagedata260 = hdulist260[1].data

hdulist262 = fits.open('images/Abell262_10884_05_wfpc2_f622w_pc_drz.fits')
imagedata262 = hdulist262[1].data

hdulist295 = fits.open('images/Abell295_08683_13_wfpc2_f814w_pc_drz.fits')
imagedata295 = hdulist295[1].data

hdulist347 = fits.open('images/Abell347_08683_14_wfpc2_f814w_pc_drz.fits')
imagedata347 = hdulist347[1].data


mpl.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman'], 'monospace': ['Computer Modern Typewriter']})
params = {'backend': 'pdf',
          'axes.labelsize': 12,
          'legend.fontsize': 12,
          'xtick.labelsize': 10,
          'ytick.labelsize': 10,
          'text.usetex': True,
          'axes.unicode_minus': True}
mpl.rcParams.update(params)
prop = fm.FontProperties(mpl.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman'],
                                           'monospace': ['Computer Modern Typewriter']}))
mpl.rcParams["mathtext.fontset"] = u"stix"


dustdata = np.loadtxt("A{}image.txt".format(abell), delimiter=" ")
mean = np.mean(dustdata)
centre = BCG[0][0], BCG[0][1]
size = 100


def cutimage(initialcentre, imagedata):
    """ Cuts Image down to size """

    a = initialcentre[0] - size
    b = initialcentre[0] + size
    c = initialcentre[1] - size
    d = initialcentre[1] + size

    datanew = imagedata[a:b, c:d]  # vertical, horizontal

    return datanew


# newimage = cutimage(centre, dustdata)
# mean = np.mean(newimage)

rotate = BCG[7][0]

if rotate == 'yes':
    newimage = np.rot90(dustdata, k=1, axes=(0, 1))


newdata76 = cutimage(centres[0], imagedata76)
newdata119 = cutimage(centres[1], imagedata119)
newdata147 = cutimage(centres[2], imagedata147)
newdata160 = cutimage(centres[3], imagedata160)
newdata168 = cutimage(centres[4], imagedata168)
newdata189 = cutimage(centres[5], imagedata189)
newdata193 = cutimage(centres[6], imagedata193)
newdata195 = cutimage(centres[7], imagedata195)
newdata260 = cutimage(centres[8], imagedata260)
newdata262 = cutimage(centres[9], imagedata262)
newdata295 = cutimage(centres[10], imagedata295)
newdata347 = cutimage(centres[11], imagedata347)

newdata = newdata76, newdata119, newdata147, newdata160, newdata168, newdata189, newdata193, newdata195, newdata260, \
          newdata262, newdata295, newdata347
# w=10
# h=10
#
# fig=plt.figure(figsize=(8, 8))
# columns = 3
# rows = 4
# for l in range(1, columns*rows):
#     img = newdata[l]
#     fig.add_subplot(rows, columns, l)
#     plt.imshow(img, cmap="gray")
#
# plt.show()

plt.figure(figsize = (4,3))
gs1 = gridspec.GridSpec(4, 3)
gs1.update(wspace=0.05, hspace=0.05)  # set the spacing between axes.


for i in range(12):
    ax1 = plt.subplot(gs1[i])
    plt.axis('on')
    img = newdata[i]
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    plt.imshow(img, cmap="gray")
    ax1.set_aspect('equal')
    ax1.tick_params(axis='None', which='None', top='False', right='False')
plt.show()


size2 = 100
fig, ax3 = plt.subplots()
ax3.axis([0, 2*size2, 0, 2*size2])
ax3.tick_params(axis='both', which='both', top='True', right='True')
plt.text(10, 180, 'Abell {}'.format(abell), fontproperties=prop, size=15, color="white")

# ax3.set_xticks([size2/2 - 80, size2/2 - 40, size2/2, size2/2 + 40, size2/2 + 80, size2/2 + 120])
# ax3.set_yticks([size2/2 - 80, size2/2 - 40, size2/2, size2/2 + 40, size2/2 + 80, size2/2 + 120])
labels = -4, -3, -2, -1, 0, 1, 2, 3, 4

ax3.set_xticklabels(labels)
ax3.set_yticklabels(labels)
ax3.get_yaxis().set_tick_params(which='both', direction='in', color="white")
ax3.get_xaxis().set_tick_params(which='both', direction='in', color="white")
ax3.set_ylabel('', fontproperties=prop, color='black', rotation=0, labelpad=20, size=18)
ax3.set_xlabel('Offset (arcsec)', fontproperties=prop, color='black', rotation=0, labelpad=20, size=16)
plt.imshow(dustdata, cmap='gray', vmin=0, vmax=mean*8, origin={'lower', 'lower'})
# plt.colorbar()
plt.show()

