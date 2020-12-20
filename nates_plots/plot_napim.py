import math
import matplotlib.pyplot as plt
import numpy as np

def nap(vm):
    if vm < -67:
        return 0
    else:
        return 1.0 / ( 1.0 + math.exp( ( -48 - vm ) / 5 ) )

def km(vm):
    if vm < -67:
        return 0
    else:
        return 1.0 / ( 1.0 + math.exp( ( -vm - 35 ) / 10.34 ) )

def nat(vm):
    if vm < -59:
        return 0
    else:
        return 1.0 / ( 1.0 + math.exp( ( -vm - 35.5) / 7.2 ) )

def kdr(vm):
    if vm < -54:
        return 0
    else:
        return 1.0 / ( 1.0 + math.exp( ( 0 - vm ) / 11 ) )
    

def cas(vm):
    if vm < -69:
        return 0
    else:
        return 1.0 / ( 1.0 +(math.exp((vm+50)/(-8.1))))

def h(vm):
    if vm < -71:
        return 1.0 / (1.0 + math.exp(-1.0 * (vm+90)/-8))
    else:
        return 0
    

def cat(vm):
    if vm < -43:
        return 0
    else:
        return 1.0 / (1.0+(math.exp((vm+27.1)/(-7.2))))

x_data = np.linspace(-100,0, 1000)
plt.figure(figsize=(5,5))
plt.plot(x_data,[nap(v) for v in x_data], label='Nap')
plt.plot(x_data,[km(v) for v in x_data], label='KM')
plt.plot(x_data,[nat(v) for v in x_data], label='Nat')
plt.plot(x_data,[kdr(v) for v in x_data], label='Kdr')
plt.plot(x_data,[h(v) for v in x_data], label='H')

plt.ylabel("Activation", fontsize=14)
plt.xlabel("V (mV)", fontsize = 16)
plt.legend(fontsize=8)
plt.tight_layout()

plt.show() 

plt.figure(figsize=(5,5))
plt.plot(x_data,[nat(v) for v in x_data], label='Nat')
plt.plot(x_data,[kdr(v) for v in x_data], label='Kdr')
plt.plot(x_data,[h(v) for v in x_data], label='H')
plt.plot(x_data,[cas(v) for v in x_data], label='Cas')
plt.plot(x_data,[cat(v) for v in x_data], label='Cat')

plt.ylabel("Activation", fontsize=14)
plt.xlabel("V (mV)", fontsize = 16)
plt.legend(fontsize=8)
plt.tight_layout()

plt.show() 