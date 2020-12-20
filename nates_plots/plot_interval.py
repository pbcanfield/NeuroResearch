import matplotlib.pyplot as plt
import numpy as np

def napkm(hz):
    if (hz >= 46 and hz <= 120):
        return 125
    else:
        return 0

def cascat(hz):
    if hz >= 116:
        return 77
    else:
        return 0

x_data = np.linspace(30, 180, 1000)
plt.figure(figsize=(5,5))
plt.plot(x_data,[napkm(v) for v in x_data], label='Nap-Km')
plt.plot(x_data,[cascat(v) for v in x_data], label='Cas-Cat-sAHP')


plt.ylabel("Max Spike Frequency (Hz)", fontsize=14)
plt.xlabel("Inter-Burst Interval (ms)", fontsize = 16)
plt.legend(fontsize=8)
plt.tight_layout()

plt.show()