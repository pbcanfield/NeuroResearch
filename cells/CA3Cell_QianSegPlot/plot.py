from neuron import h
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

h.load_file('stdrun.hoc')
h.load_file('cell_plotter.hoc')

def i_inj_plot(t):
    if t <= 400 or t >= 1400:
        return 0
    else:
        return 0.8

trace = h.membrane_voltage.as_numpy()
time = h.time.as_numpy()
inj = np.array([i_inj_plot(t) for t in time])

current_inj = h.current_inj.as_numpy()
fi = h.reported.as_numpy()

plt.rcParams['font.size'] = '16'

fig = plt.figure(figsize = (7,5))
gs = mpl.gridspec.GridSpec(2, 1, height_ratios=[4,1])

ax = plt.subplot(gs[0])
ax.set_xticks([])
for label in ax.get_yticklabels():
    label.set_fontsize(16)
ax.set_yticks([-75, -50, -25, 0, 25])
#fig.suptitle('No Segregation', fontsize=20)
plt.plot(time, trace, color = 'red', lw = 0.9)
plt.ylabel('Voltage (mV)', fontsize=20)




ax = plt.subplot(gs[1])
for label in ax.get_yticklabels():
    label.set_fontsize(16)
ax.set_yticks([0, 0.8])
plt.plot(time, inj, color = 'black', lw = 0.9)
plt.ylabel('Current (nA)', fontsize=20)
plt.xlabel('Time (ms)', fontsize=20)
plt.tight_layout()
plt.show()