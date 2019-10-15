import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
slope = -0.046, 0.044, 0.15, 0.27, 0.0013, -0.026
rb = 10.76*0.05, 7.32*0.05, 6.15*0.05, 2.53*0.05, 10.31*0.05, 8.52*0.05
ms = [31.8, 30.6, 29, 29.6, 31.85, 31.05]
# plt.figure()
# rb = np.log(rb)
# plt.plot(rb, slope, 'x')
# plt.show()
# plt.figure()
# rb = np.log(rb)
# plt.plot(ms, slope, 'x')
# plt.show()

import os
fpath = os.path.join(rcParams["datapath"], "fonts/ttf/nimbusmono-bold.ttf")
prop = fm.FontProperties(fname=fpath)
fname = os.path.split(fpath)[1]
print(prop)
fig, ax1 = plt.subplots()
ax1.plot(slope, ms, 'b.')
ax1.set_xlabel('$\Gamma_{0.05}$')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('M')
ax1.tick_params('y')
ax1.get_yaxis().set_tick_params(which='both', direction='in')
ax1.get_xaxis().set_tick_params(which='both', direction='in')

ax2 = ax1.twinx()
ax2.get_yaxis().set_tick_params(which='both', direction='in')
ax2.get_xaxis().set_tick_params(which='both', direction='in')
ax2.plot(slope, rb, 'r.')
ax2.set_ylabel('r$_b$')
ax2.tick_params('y')

fig.tight_layout()
plt.show()
