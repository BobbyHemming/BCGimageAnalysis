import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib import font_manager as fm, rcParams
from ClusterParams import galaxylist as glist
import matplotlib as mpl
from numpy import arange,array,ones
from scipy import stats
import itertools


# fpath = os.path.join(rcParams["datapath"], "fonts/ttf/nimbusmono-bold.ttf")
# prop = fm.FontProperties(fname=fpath)
# fname = os.path.split(fpath)[1]
# print(prop)

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

abell = 3676
data = np.loadtxt("datafiles/A{}.txt".format(abell))
# dustdata = np.loadtxt("datafiles/dustlist.txt").readlines()
dustdata = np.loadtxt("datafiles/dustlist.txt", delimiter=",")
bcgdetails = np.loadtxt("BCGs.txt", delimiter="&")


rarcsecs = data[0]
imagem = data[1]
modelm = data[2]
dustmodifiedm = data[3]
nodustmodel = data[4]

n = 76, 119, 147, 160, 168, 189, 193, 195, 260, 262, 295, 347, 376, 397, 419, 496, 533, 548, 634, 671, 779, 912, \
    999, 1016, 1060, 1142, 1177, 1228, 1308, 1314, 1367, 1631, 1656, 1795, 1836, 1983, 2040, 2052, 2147, 2162, 2197, \
    2247, 2572, 2589, 2593, 2634, 2657, 2666, 2877, 3144, 3193, 3376, 3395, 3526, 3528, 3532, 3554, 3556, 3558, 3559,\
    3562, 3564, 3565, 3571, 3574, 3656, 3676, 3677, 3698, 3716, 3733, 3736, 3742, 3744, 3747, 4038, 4049, 4059


irlist = np.zeros((len(glist), 4))  # This is in Vega Magnitudes, needs conv. to flux and luminosity
np.seterr(all='raise')


def chicalc(xi, mi):
    """Chi Squared calculator"""
    chisq = np.sum(((xi - mi)**2)/0.2)
    return chisq


chi2 = []
for z in range(len(glist)):
    obsv = np.loadtxt("datafiles/A{}.txt".format(n[z]))[1]
    exp = np.loadtxt("datafiles/A{}.txt".format(n[z]))[2]
    chi2.append(chicalc(obsv, exp))

print(chi2)
print(np.sum(chi2)/len(glist))


def sbpfinalplot(x, yimage, ymodel, ydust, n):

    xs, ys, ymod, ydm = x, yimage, ymodel, ydust
    xmin, xmax = 0, max(xs) + 2 * max(xs)
    ymin, ymax = min(ys) - 0.05 * min(ys), max(ys) + 0.05 * max(ys)

    fig = plt.figure()
    ax1 = fig.add_axes([0.15, 0.3, 0.7, 0.6])
    ax1.set_xscale("log")
    ax1.plot(xs, ys, marker='s', color='black', ms=3)
    ax1.plot(xs, ymod)
    ax1.plot(xs, ydm, color='orange')

    plt.text(0.05 * xmax, ymin + 1, 'Abell {}'.format(n), fontproperties=prop, size=15)
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
    ax2.semilogx(xs, ydm - ys, color='orange')  # Must be the same as in axes 3
    # ax2.semilogx(xs, ydm - ymod, color='orange')  # Must be the same as in axes 3
    ax2.axis([xmin, xmax, -0.2, 0.2])
    ticks = 0.1, 0, -0.1
    ax2.set_yticks(ticks, minor=False)
    ax2.get_yaxis().set_tick_params(which='both', direction='in')
    ax2.get_xaxis().set_tick_params(which='both', direction='in')
    ax2.tick_params(axis='both', which='both', top='True', right='True')
    ax2.set_xlabel('R (arcseconds)', fontproperties=prop, color='black', size=12)
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


# def sbpfinalplot2(x, yimage, ymodel, ydust):
#
#     xs, ys, ymod, ydm = x, yimage, ymodel, ydust
#     xmin, xmax = 0, max(xs) + 2 * max(xs)
#     ymin, ymax = min(ys) - 0.05 * min(ys), max(ys) + 0.05 * max(ys)
#
#     fig = plt.figure()
#     ax1 = fig.add_axes([0.15, 0.3, 0.7, 0.6])
#     ax1.set_xscale("log")
#     ax1.plot(xs, ys, marker='s', color='black', ms=3)
#     # ax1.plot(xs, ymod)
#     # ax1.plot(xs, ydm, color='orange')
#
#     plt.text(0.05 * xmax, ymin + 1, 'Abell{}'.format(abell), fontproperties=prop, size=15)
#     ax1.axis([xmin, xmax, ymax, ymin])
#     # ax1.set_yscale("log")
#     ax1.get_yaxis().set_tick_params(which='both', direction='in')
#     ax1.get_xaxis().set_tick_params(which='both', direction='in')
#     ax1.tick_params(axis='both', which='both', top='True', right='True')
#     ax1.tick_params(labelbottom=True)
#     ax1.set_yticklabels(ax1.get_yticks(), fontproperties=prop, size=12)
#     ax1.set_ylabel('M', fontproperties=prop, color='black', rotation=0, labelpad=28, size=13)
#     # ax1.set_title('Surface Brightness Profile', fontproperties=prop, color='black', size=12)
#     ax1.set_xlabel('R [arcseconds]', fontproperties=prop, color='black', size=12)
#
#     # ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.2])
#     # ax2.semilogx(xs, ymod - ys)  # Must be the same as in axes 3
#     # ax2.semilogx(xs, ydm - ymod, color='orange')  # Must be the same as in axes 3
#     # ax2.axis([xmin, xmax, -0.2, 0.2])
#     # ticks = 0.1, 0, -0.1
#     # ax2.set_yticks(ticks, minor=False)
#     # ax2.get_yaxis().set_tick_params(which='both', direction='in')
#     # ax2.get_xaxis().set_tick_params(which='both', direction='in')
#     # ax2.tick_params(axis='both', which='both', top='True', right='True')
#     # ax2.set_xlabel('R [arcseconds]', fontproperties=prop, color='black', size=12)
#     # ax2.set_xticklabels(ax2.get_xticks(), fontproperties=prop, size=12)
#     # ax2.set_yticklabels(ax2.get_yticks(), fontproperties=prop, size=11)
#     # ax2.set_ylabel('$\Delta$M', fontproperties=prop, color='black', rotation=0, labelpad=16, size=12)
#     #
#     # ax3 = fig.add_axes((0.15, 0.2, 0.7, 0.1))
#     # ax3.yaxis.set_visible(False)
#     # ax3.get_xaxis().set_tick_params(which='both', direction='inout')
#     # ax3.tick_params(labelbottom=False)
#     # ax3.set_xscale("log")
#     # ax3.axis([xmin, xmax, 0, 0.1])
#     # ax3.set_xlim(ax1.get_xlim()[0], ax1.get_xlim()[1])
#     # ax3.spines['bottom'].set_position('zero')
#     # ax3.patch.set_alpha(0)
#
#     for axis in [ax1.xaxis, ax1.yaxis]:
#         axis.set_major_formatter(ScalarFormatter())
#     # for axis in [ax2.xaxis, ax2.yaxis]:
#     #     axis.set_major_formatter(ScalarFormatter())
#
#     plt.show()
#
#     return 1


# sbpfinalplot(rarcsecs, imagem, nodustmodel, dustmodifiedm)


for i in range(len(glist)):
    irlist[i, 0] = glist[i][10][0]
    irlist[i, 1] = glist[i][10][1]
    irlist[i, 2] = glist[i][10][2]
    irlist[i, 3] = glist[i][10][3]


def magtoflux(w1to4mags):

    w1flux = 309.54 * 10 ** (-w1to4mags[0] / 2.5)
    w2flux = 171.787 * 10 ** (-w1to4mags[1] / 2.5)
    w3flux = 31.674 * 10 ** (-w1to4mags[2] / 2.5)
    w4flux = 8.363 * 10 ** (-w1to4mags[3] / 2.5)

    # w1flux = 10 ** (-w1to4mags[0] / 2.5)
    # w2flux = 10 ** (-w1to4mags[1] / 2.5)
    # w3flux = 10 ** (-w1to4mags[2] / 2.5)
    # w4flux = 10 ** (-w1to4mags[3] / 2.5)

    w1to4flux = w1flux, w2flux, w3flux, w4flux

    return w1to4flux


def magtoluminosity(w1to4mags, D):

    flux12 = magtoflux(w1to4mags)[2]          # 12 micrometers + 5.174
    flux24 = magtoflux(w1to4mags)[3]         # 24 micrometers  + 6.620

    flux15 = (3/12)*(flux24 - flux12) + flux12
    r = D * 3.08567758128 * (10 ** 22)

    lum15 = (4*np.pi*r**2)*flux15
    irlum = 11.1*(15*(10**-6)*lum15)**0.998

    return irlum


fluxlist = np.zeros((len(glist), 4))
fratio4_3 = []
fratio24_12 = []
fratio12_4 = []
fratio24_3 = []
fratio24_4 = []

fluxratiog6 = []
fluxratiog42_6 = []
fluxratiog375_42 = []
fluxratiog34_375 = []
fluxratiog31_34 = []
fluxratiog29_31 = []
fluxratiog2_29 = []
label6 = []
label42_6 = []
label375_42 = []
label34_375 = []
label31_34 = []
label29_31 = []
label2_29 = []


dustfratio12_4 = []
dustfratio24_3 = []
nodustfratio12_4 = []
nodustfratio24_3 = []
# The flux ratios for each w band (1, 2, 3, 4).
for j in range(len(glist)):

    fluxlist[j, :] = magtoflux(irlist[j])

    print(100*fluxlist[j, :])

    fratio4_3.append(fluxlist[j, 1]/fluxlist[j, 0])

    fratio24_12.append(fluxlist[j, 3]/fluxlist[j, 2])

    fratio12_4.append(fluxlist[j, 2]/fluxlist[j, 1])

    fratio24_3.append(fluxlist[j, 3]/fluxlist[j, 0])

    fratio24_4.append(fluxlist[j, 3]/fluxlist[j, 1])

    if dustdata[j, 1] >= 1.5*10**5:
        dustfratio12_4.append(fluxlist[j, 2]/fluxlist[j, 1])
        dustfratio24_3.append(fluxlist[j, 3]/fluxlist[j, 0])
    else:
        nodustfratio12_4.append(fluxlist[j, 2]/fluxlist[j, 1])
        nodustfratio24_3.append(fluxlist[j, 3]/fluxlist[j, 0])



dustinfluxband = []
for k in range(len(glist)):
    nfratio12_4 = fluxlist[k, 2]/fluxlist[k, 1]
    if nfratio12_4 >= 0.6:
        fluxratiog6.append(fluxlist[k, :])
        label6.append(k)
    elif 0.42 <= nfratio12_4 <= 0.6:
        fluxratiog42_6.append(fluxlist[k, :])
        label42_6.append(k)
    elif 0.375 <= nfratio12_4 <= 0.42:
        fluxratiog375_42.append(fluxlist[k, :])
        label375_42.append(k)
    elif 0.34 <= nfratio12_4 <= 0.375:
        fluxratiog34_375.append(fluxlist[k, :])
        label34_375.append(k)
    elif 0.31 <= nfratio12_4 <= 0.34:
        fluxratiog31_34.append(fluxlist[k, :])
        label31_34.append(k)
    elif 0.2 <= nfratio12_4 <= 0.31:
        fluxratiog29_31.append(fluxlist[k, :])
        label29_31.append(k)
        dustinfluxband.append(dustdata[k, 1])
    # elif 0.2 <= nfratio12_4 <= 0.29:
    #     fluxratiog2_29.append(fluxlist[k, :])
    #     label2_29.append(k)


irluminositylist = np.zeros(len(glist))
for b in range(len(glist)):
    irluminositylist[b] = magtoluminosity(irlist[b], glist[b][9])


sunlum = 3.839*10**33
A = 1.57*10**-10
SFRir = A*(irluminositylist/sunlum)*(1+np.sqrt((10**9)*(sunlum/irluminositylist)))
print(SFRir)


def plot(a):

    wband = 3.4, 4.6, 12, 22
    fig, ax = plt.subplots()
    # ax.axis([2, 50, 0.1, 1200])
    ax.loglog()

    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_major_formatter(ScalarFormatter())

    for i in range(len(glist)):
        plt.plot(wband, a[i]/a[i][0])

    plt.show()

    return 1


def SED(SED, label):

    wband = 3.4, 4.6, 12, 22
    fig, ax = plt.subplots()
    ax.axis([2, 50, 0.1, 10])
    ax.loglog()

    plt.text(3, 6, r'$F_{12\mu m} / F_{4.4\mu m}\leq0.31$', fontproperties=prop, size=15)
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_major_formatter(ScalarFormatter())
    ax.tick_params(axis='both', which='both', top='True', right='True')
    ax.get_yaxis().set_tick_params(which='both', direction='in')
    ax.get_xaxis().set_tick_params(which='both', direction='in')

    plt.plot(wband, SED[0] / SED[0][0], label="Abell {}".format(n[label[0]]), color="black", marker='s', linestyle="--", linewidth=0.7)
    plt.plot(wband, SED[1] / SED[1][0], label="Abell {}".format(n[label[1]]), color="black", marker='o', linestyle="-.", linewidth=0.7)
    plt.plot(wband, SED[2] / SED[2][0], label="Abell {}".format(n[label[2]]), color="black", marker='x', linestyle="-", linewidth=0.7)
    plt.plot(wband, SED[3] / SED[3][0], label="Abell {}".format(n[label[3]]), color="black", marker='+', linestyle="-", linewidth=0.7)
    plt.plot(wband, SED[4] / SED[4][0], label="Abell {}".format(n[label[4]]), color="black", marker="^", linestyle=":", linewidth=0.7)
    plt.plot(wband, SED[5] / SED[5][0], label="Abell {}".format(n[label[5]]), color="black", marker='.', linestyle="--", linewidth=0.7)
    plt.plot(wband, SED[6] / SED[6][0], label="Abell {}".format(n[label[6]]), color="black", marker='h', linestyle="-.", linewidth=0.7)
    plt.plot(wband, SED[7] / SED[7][0], label="Abell {}".format(n[label[7]]), color="black", marker='D', linestyle="-", linewidth=0.7)
    plt.plot(wband, SED[8] / SED[8][0], label="Abell {}".format(n[label[8]]), color="black", marker='d', linestyle="-", linewidth=0.7)
    plt.plot(wband, SED[9] / SED[9][0], label="Abell {}".format(n[label[9]]), color="black", marker="X", linestyle=":", linewidth=0.7)
    plt.plot(wband, SED[10] / SED[10][0], label="Abell {}".format(n[label[10]]), color="black", marker='*', linestyle="", linewidth=0.7)
    plt.plot(wband, SED[11] / SED[11][0], label="Abell {}".format(n[label[11]]), color="black", marker='p', linestyle="-.", linewidth=0.7)
    plt.plot(wband, SED[12] / SED[12][0], label="Abell {}".format(n[label[12]]), color="black", marker='P', linestyle="-", linewidth=0.7)
    plt.plot(wband, SED[13] / SED[13][0], label="Abell {}".format(n[label[13]]), color="black", marker="H", linestyle=":",linewidth=0.7)
    plt.plot(wband, SED[14] / SED[14][0], label="Abell {}".format(n[label[14]]), color="black", marker='.',linestyle="--", linewidth=0.7)
    plt.plot(wband, SED[15] / SED[15][0], label="Abell {}".format(n[label[15]]), color="black", marker=',', linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[16] / SED[16][0], label="Abell {}".format(n[label[16]]), color="black", marker="s", linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[17] / SED[17][0], label="Abell {}".format(n[label[17]]), color="black", marker="o", linestyle="--",linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[18] / SED[18][0], label="Abell {}".format(n[label[18]]), color="black", marker="^",linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[19] / SED[19][0], label="Abell {}".format(n[label[19]]), color="black", marker="h",linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[20] / SED[20][0], label="Abell {}".format(n[label[20]]), color="black", marker="D",linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[21] / SED[21][0], label="Abell {}".format(n[label[21]]), color="black", marker="d",
             linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[22] / SED[22][0], label="Abell {}".format(n[label[22]]), color="black", marker="X",
             linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[23] / SED[23][0], label="Abell {}".format(n[label[23]]), color="black", marker="p",
             linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[24] / SED[24][0], label="Abell {}".format(n[label[24]]), color="black", marker="P",
             linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[25] / SED[25][0], label="Abell {}".format(n[label[25]]), color="black", marker="*",
             linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.plot(wband, SED[26] / SED[26][0], label="Abell {}".format(n[label[26]]), color="black", marker="H",
             linestyle="--", linewidth=0.7, markerfacecolor='none')
    plt.xlabel(r'Observed Wavelength ($\mu m$)', fontproperties=prop, color='black', rotation=0, labelpad=18, size=18)
    plt.ylabel(r'Normalised Flux (erg cm$^{-2}$ s${^-1})$', fontproperties=prop, color='black', rotation=90, labelpad=18, size=18)
    ax.legend(prop={'size': 7})
    plt.legend(frameon=False)
    plt.show()

    return 1


print(np.sum(dustinfluxband)/len(dustinfluxband))

# SED(fluxratiog6, label6)
# SED(fluxratiog42_6, label42_6)
# SED(fluxratiog375_42, label375_42)
# SED(fluxratiog34_375, label34_375)
# SED(fluxratiog31_34, label31_34)
# SED(fluxratiog29_31, label29_31)


# plot(fluxlist)
print(sum(dustdata[:, 1])/78)

fig, ax = plt.subplots()
ax.axis([0.18, 1.5, 0.08, 1.3])
ax.loglog()
# plt.plot((0.5, 0.5), (0, 10), linestyle="--", color="grey", linewidth="0.8")
#
# plt.plot((0, 10), (0.5, 0.5), linestyle="--", color="grey", linewidth="0.8")
ax.tick_params(axis='both', which='both', top='True', right='True')
ax.get_yaxis().set_tick_params(which='both', direction='in')
ax.get_xaxis().set_tick_params(which='both', direction='in')
plt.xlabel(r'$F_{12\mu m} / F_{4.6\mu m}$', fontproperties=prop, color='black', rotation=0, labelpad=16, size=15)
plt.ylabel(r'$F_{24\mu m} / F_{3\mu m}$', fontproperties=prop, color='black', rotation=0, labelpad=16, size=15)
plt.plot(dustfratio12_4, dustfratio24_3, linestyle='', color="black", marker="^", ms=4.5)
plt.plot(nodustfratio12_4, nodustfratio24_3, linestyle='', color="black", marker="s", markerfacecolor='none', ms=4.5)
# plt.plot(fratio12_4, fratio24_12, linestyle='', color="black", marker="s", markerfacecolor='none', ms=4.5)
for axis in [ax.xaxis, ax.yaxis]:
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    axis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_major_formatter(ScalarFormatter())
plt.show()

# fig, ax = plt.subplots()
# # ax.axis([0.18, 2, 0.1, 3])
# ax.loglog()
# for axis in [ax.xaxis, ax.yaxis]:
#     axis.set_major_formatter(ScalarFormatter())
# plt.plot((0.5, 0.5), (0, 10), linestyle="--", color="grey")
# plt.plot((0, 10), (1, 1), linestyle="--", color="grey")
#
# plt.xlabel(r'$F_{12\mu m} / F_{4.6\mu m}$', fontproperties=prop, color='black', rotation=0, labelpad=16, size=12)
# plt.ylabel(r'$F_{24\mu m} / F_{3\mu m}$', fontproperties=prop, color='black', rotation=0, labelpad=16, size=12)
# plt.plot(fratio12_4, fratio24_3, linestyle='', marker='+' )
# plt.show()

kpc2 = (1/np.pi)*(np.pi*bcgdetails[:, 1]*10**3/(3600*180))**0.5
fig, ax2 = plt.subplots()
plt.plot(fratio12_4, dustdata[:, 1], linestyle="", marker=".", color="black", ms=2)
plt.plot(fratio12_4, dustdata[:, 1], linestyle="", marker="o", color="black", ms=4, markerfacecolor='none')
# plt.plot((1.0, 19.1631), (26254.7, 2.82*10**8), linestyle="-", color="black", linewidth="0.8")
ax2.set_xscale("log")
ax2.set_yscale("log")
# logA = np.log(SFRir+1)
# logB = np.log(100*(dustdata[:, 1]+1))
# m, c = np.polyfit(logA, logB, 1)  # fit log(y) = m*log(x) + c
# print(m, c)
# y_fit = np.exp(m*logA + c)        # calculate the fitted values of y
# z = np.linspace(0, 100, len(dustdata[:, 1]))
# plt.plot(SFRir+1, y_fit, linestyle='-', color="black")
plt.xlabel(r'$F_{12\mu m} / F_{4.6\mu m}$', fontproperties=prop, color='black', rotation=0, labelpad=16, size=15)
plt.ylabel(r'$M_d  (M_{\odot})$', fontproperties=prop, color='black', rotation=90, labelpad=16, size=15)
# plt.plot(SFRir+1, 100*dustdata[:, 1], linestyle='', color="black", marker="s", markerfacecolor='none', ms=4.5)
# for axis in [ax2.xaxis]:
#     formatter = ScalarFormatter()
#     formatter.set_scientific(False)
#     axis.set_major_formatter(formatter)
ax2.tick_params(axis='both', which='both', top='True', right='True')
ax2.get_yaxis().set_tick_params(which='both', direction='in')
ax2.get_xaxis().set_tick_params(which='both', direction='in')
for t, txt in enumerate(n):
    ax2.annotate(txt, (SFRir[t] + 1, 100*dustdata[:, 1][t]))
plt.show()



SFRd = []
SFRi = []
kpcnew = []
SFRdust = dustdata[:, 1]*100*2.5*1.8*10**(-8)
for p in range(len(glist)):
    if dustdata[p, 1] >= 11:
        SFRd.append(dustdata[p, 1])
        SFRi.append(SFRir[p])
        kpcnew.append(kpc2[p])

yerror = np.linspace(0.9, 1.1, len(glist))*500
SFRi = np.array(SFRi)
SFRd = np.array(SFRd)
kpcnew = np.array(kpcnew)
# SFRi = A*(irluminositylist/sunlum)*(1+np.sqrt((10**9)*(sunlum/irluminositylist)))
fig, ax2 = plt.subplots()
mhkenneticut = (kpcnew**0.57)*((1/1.8)*10**8)*SFRi**0.71
mh2 = (20)*2.5*100*SFRd/(np.pi*(kpcnew)**2)
plt.plot(SFRi, mh2, linestyle="", marker=".", color="black", ms=1)
plt.plot(SFRi, mh2, linestyle="", marker="s", color="black", ms=5, markerfacecolor='none')
ax2.errorbar(SFRi, mh2, yerr=0.5*mh2, linestyle="")
# plt.plot(SFRi, 20*mhkenneticut, linestyle="", marker="^", color="blue", ms=5)
# plt.plot(SFRi, 10*mhkenneticut, linestyle="", marker="^", color="green", ms=5)
# plt.plot(SFRi, 50*mhkenneticut, linestyle="", marker="^", color="orange", ms=5)
plt.plot((0.3146, 13.17631), (201498, 4.61*10**6), linestyle="--", color="black", linewidth="0.6")
plt.plot((0.340549, 12.1631), (4.333*10**8, 8.8012*10**9), linestyle="--", color="grey", linewidth="0.6", label=r"$d_{50kpc}$")
plt.plot((0.340483, 12.1588), (1.73736*10**8, 3.53082*10**9), linestyle=":", color="grey", linewidth="0.7", label=r"$d_{20kpc}$")
plt.plot((0.340456, 12.1656), (8.63273*10**7, 1.76617*10**9), linestyle="-.", color="grey", linewidth="0.8", label=r"$d_{10kpc}$")
ax2.set_xscale("log")
ax2.set_yscale("log")
x = np.linspace(0.01, 10, len(SFRi))

logA = np.log(SFRi)
logB = np.log(mh2)
m, c = np.polyfit(logA, logB, 1)  # fit log(y) = m*log(x) + c
print(m, c)
y_fit = np.exp(m*logA + c)        # calculate the fitted values of y
z = np.linspace(0, 100, len(dustdata[:, 1]))
plt.plot(SFRi, y_fit, linestyle='-', color="black")

plt.xlabel(r'$\Psi_{IR}(M_{\odot}yr^{-1})$', fontproperties=prop, color='black', rotation=0, labelpad=16, size=15)
plt.ylabel(r'mH$_2 (M_{\odot})$', fontproperties=prop, color='black', rotation=90, labelpad=16, size=15)
# plt.plot(SFRir+1, 100*dustdata[:, 1], linestyle='', color="black", marker="s", markerfacecolor='none', ms=4.5)
for axis in [ax2.xaxis]:
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    axis.set_major_formatter(formatter)
ax2.tick_params(axis='both', which='both', top='True', right='True')
ax2.get_yaxis().set_tick_params(which='both', direction='in')
ax2.get_xaxis().set_tick_params(which='both', direction='in')

# for t, txt in enumerate(n):
#     ax2.annotate(txt, (SFRir[t] + 1, 100*dustdata[:, 1][t]))
plt.legend(frameon=False)
plt.show()


# fig, ax3 = plt.subplots()
# ax3.tick_params(axis='both', which='both', top='True', right='True')
# ax3.get_yaxis().set_tick_params(which='both', direction='in')
# ax3.get_xaxis().set_tick_params(which='both', direction='in')
# ax3.set_ylabel('N', fontproperties=prop, color='black', rotation=0, labelpad=20, size=18)
# ax3.set_xlabel('z', fontproperties=prop, color='black', rotation=0, labelpad=20, size=20)
# x = bcgdetails[:, 0]/(3*10**5)
# num_bins = 15
# n, bins, patches = plt.hist(x, num_bins, facecolor='dimgrey', alpha=0.4, edgecolor='black', linewidth=0.9)
# plt.show()

def deriv(xs, ys):
    dx = xs[1] - xs[0]
    dydx = np.gradient(ys, dx)

    return dydx


slopelum = np.zeros((len(glist), 2))
slope = np.zeros(len(glist))

hollow = []
nothollow = []
excess = []

for m in range(len(glist)):
    mags = (np.loadtxt("datafiles/A{}.txt".format(n[m]))[1])
    slope[m] = -(mags[1]-mags[0])/(np.log(rarcsecs[1]-rarcsecs[0]))
    slopelum[m, 0] = slope[m]*2.5
    slopelum[m, 1] = bcgdetails[m, 2]

    fratio12to4 = fratio12_4[m]
    fratio24to3 = fratio24_3[m]

    if slope[m] <= 0:
        hollow.append(slopelum[m, :])
    elif fratio12to4 >= 0.5:
        excess.append(slopelum[m, :])
    elif fratio24to3 >= 0.5:
        excess.append(slopelum[m, :])
    else:
        nothollow.append(slopelum[m, :])

    # sbpfinalplot(np.loadtxt("datafiles/A{}.txt".format(n[m]))[0], np.loadtxt("datafiles/A{}.txt".format(n[m]))[1],
    #              np.loadtxt("datafiles/A{}.txt".format(n[m]))[2], np.loadtxt("datafiles/A{}.txt".format(n[m]))[3], n[m])


hollow = np.array(hollow)
nothollow = np.array(nothollow)
excess = np.array(excess)
fig, ax4 = plt.subplots()
ax4.axis([-21.3, -25.3, -0.1, 0.5])
plt.plot((-19, -26), (0.3, 0.3), linestyle="--", color="grey", linewidth="0.8")
plt.plot((-19, -26), (0, 0), color="black", linewidth="0.8")
plt.plot(nothollow[:,1], nothollow[:,0], linestyle='', marker="+", color='black')
plt.plot(hollow[:,1], hollow[:,0], linestyle='', marker="^", color='black', ms=3)
plt.plot(excess[:,1], excess[:,0], linestyle='', marker="o", color='black', ms=3)
ax4.tick_params(axis='both', which='both', top='True', right='True')
ax4.get_yaxis().set_tick_params(which='both', direction='in')
ax4.get_xaxis().set_tick_params(which='both', direction='in')
plt.xlabel(r'$M_V$', fontproperties=prop, color='black', rotation=0, labelpad=16, size=16)
plt.ylabel(r'$\Gamma_{r\rightarrow 0}$', fontproperties=prop, color='black', rotation=0, labelpad=16, size=16)
plt.show()




rb = (np.pi*bcgdetails[:, 4]/(3600*180))*bcgdetails[:, 1]*(10**6)
# slope, intercept, r_value, p_value, std_err = stats.linregress(bcgdetails[:, 2], np.log(rb))
# line = slope*bcgdetails[:, 2]+intercept


fig, ax5 = plt.subplots()
ax5.axis([-21.3, -25.1, 10, 1500])
plt.plot((-18.65, -25.65), (10, 1600), linestyle="-", color="black", linewidth="0.8")
plt.plot((-19, -26), (50, 50), linestyle="-.", color="darkgray", linewidth="0.8")
plt.plot((-22, -22), (10, 1600), linestyle="--", color="darkgray", linewidth="0.8")
plt.plot(bcgdetails[:, 2], rb, marker="+", color='black', linestyle="")
rblog = np.log(rb)
plt.plot(np.unique(bcgdetails[:, 2]), np.poly1d(np.polyfit(bcgdetails[:, 2], rblog, 1))(np.unique(bcgdetails[:, 2])))
ax5.set_yscale("log")
ax5.tick_params(axis='both', which='both', top='True', right='True')
ax5.get_yaxis().set_tick_params(which='both', direction='in')
ax5.get_xaxis().set_tick_params(which='both', direction='in')
for axis in [ax5.xaxis, ax5.yaxis]:
    axis.set_major_formatter(ScalarFormatter())
plt.xlabel(r'$M_V$', fontproperties=prop, color='black', rotation=0, labelpad=16, size=16)
plt.ylabel(r'$r_b$(pc)', fontproperties=prop, color='black', rotation=0, labelpad=16, size=16)
plt.show()


fig, ax6 = plt.subplots()
ax6.axis([10, 1400, -0.1, 0.5])
plt.plot((0, 1500), (0, 0), linestyle="-.", color="darkgray", linewidth="0.8")
plt.plot((0, 1500), (0, 0), linestyle="-.", color="darkgray", linewidth="0.8")
plt.plot(rb, 2.5*slope, marker="+", color='black', linestyle="")
ax6.set_xscale("log")
ax6.tick_params(axis='both', which='both', top='True', right='True')
ax6.get_yaxis().set_tick_params(which='both', direction='in')
ax6.get_xaxis().set_tick_params(which='both', direction='in')
for axis in [ax6.xaxis, ax6.yaxis]:
    axis.set_major_formatter(ScalarFormatter())
plt.xlabel(r'$r_b$(pc)', fontproperties=prop, color='black', rotation=0, labelpad=16, size=16)
plt.ylabel(r'$\Gamma_{r\rightarrow 0}$', fontproperties=prop, color='black', rotation=0, labelpad=16, size=16)
plt.show()


dustirlist = []
for y in range(len(glist)):
    if dustdata[y] >= 10:
        dustirlist[y, 0] = (int(n[y]))
        dustirlist[y, 1] = dustdata[y, 1]
        dustirlist[y, 2] = irluminositylist[y]


fig, ax7 = plt.subplots()
ax7.axis([3*10**42, 3*10**44, 100, 5*10**6])
logA = np.log(irluminositylist)
logB = np.log(dustdata[:, 1] + 1)

m, c = np.polyfit(logA, logB, 1)  # fit log(y) = m*log(x) + c
y_fit = np.exp(m*logA + c)  # calculate the fitted values of y

plt.plot(irluminositylist, dustdata[:, 1]+1, "x", color="black")
plt.plot(irluminositylist, y_fit, ":", color="black")
ax7.set_yscale("log")
ax7.set_xscale("log")
plt.show()
