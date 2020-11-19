from neuron import h
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

h.load_file('stdrun.hoc')
h.load_file('cell_plotter.hoc')

def i_inj_plot(t):
    if t <= 400 or t >= 900:
        return 0
    else:
        return 0.3

trace = h.membrane_voltage.as_numpy()
time = h.time.as_numpy()
inj = np.array([i_inj_plot(t) for t in time])


fig = plt.figure(figsize = (7,5))
gs = mpl.gridspec.GridSpec(2, 1, height_ratios=[4, 1])
ax = plt.subplot(gs[0])
plt.plot(time, trace, color = 'red', lw = 0.9)
plt.ylabel('voltage (mV)')
ax.set_xticks([])
ax.set_yticks([-80, -20, 40])

ax = plt.subplot(gs[1])
plt.plot(time, inj, color = 'black', lw = 0.9)
plt.ylabel('voltage (mV)')
plt.xlabel('time (ms)')

plt.show()