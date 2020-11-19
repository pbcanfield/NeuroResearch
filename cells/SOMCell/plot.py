from neuron import h
import numpy as np
import matplotlib.pyplot as plt

h.tstop = 1000

soma = h.Section(name='Soma')

dendrites = []
dendrites.append(h.Section(name='dend1'))
dendrites.append(h.Section(name='dend2'))


gnat   = 0.04
gkdr   = 0.009
ga     = 0.0001
cattau = 10
glca   = 0.1
gcat   = 0.0005
gsahp  = 5e-5


soma.insert('IAOLM')
soma.insert('ichan2OLM')
soma.insert('ccanlOLM')
soma.insert('lcaOLM')
soma.insert('catOLM')

for dend in dendrites:
    dend.insert('IAOLM')
    dend.insert('ichan2OLM')
    dend.insert('ccanlOLM')
    dend.insert('lcaOLM')
    dend.insert('catOLM')

dendrites[0].connect(soma(0), 0)
dendrites[1].connect(soma(1), 0)

soma.nseg = 1
soma.L = 20
soma.diam = 10
soma.cm = 1
soma.Ra = 150

dendrites[0].nseg = 1
dendrites[0].L = 250
dendrites[0].diam = 3
dendrites[0].cm = 1.3
dendrites[0].Ra = 150

dendrites[1].nseg = 1
dendrites[1].L = 250
dendrites[1].diam = 3
dendrites[1].cm = 1.3
dendrites[1].Ra = 150

gnat   = 0.04
gkdr   = 0.009
ga     = 0.0001
cattau = 10
glca   = 0.1
gcat   = 0.0005
gsahp  = 5e-5

soma.gkAbar_IAOLM = ga
soma.gnatbar_ichan2OLM= gnat
soma.gkfbar_ichan2OLM= gkdr
soma.gl_ichan2OLM = 3e-5
soma.catau_ccanlOLM = cattau
soma.caiinf_ccanlOLM = 5.e-6
soma.glcabar_lcaOLM= glca
soma.gcatbar_catOLM = gcat
soma.enat = 55
soma.ekf = -90
soma.ek = -90
soma.elca = 130

for dend in dendrites:
    dend.gkAbar_IAOLM = ga
    dend.gnatbar_ichan2OLM= gnat
    dend.gkfbar_ichan2OLM= gkdr
    dend.gl_ichan2OLM = 3e-5
    dend.catau_ccanlOLM = cattau
    dend.caiinf_ccanlOLM = 5.e-6
    dend.glcabar_lcaOLM= glca
    dend.gcatbar_catOLM = gcat
    dend.enat = 55
    dend.ekf = -90
    dend.ek = -90
    dend.elca = 130

n_trace = h.Vector()
n_time = h.Vector()
n_trace.record(soma(0.5)._ref_v)
n_time.record(h._ref_t)


iclamp = h.IClamp(soma(0.5))
iclamp.dur = 400
iclamp.delay = 500
iclamp.amp = 0.3

h.run()

def i_inj_plot(t):
    if t <= 500 or t >= 900:
        return 0.3
    else:
        return 0

trace = n_trace.as_numpy()
time = n_time.as_numpy()
inj = np.array([i_inj_plot(t) for t in time])


fig,axs = plt.subplots(2)
axs[0].plot(time, trace, color = 'red')
axs[1].plot(time, inj, color = 'black')

plt.show()
