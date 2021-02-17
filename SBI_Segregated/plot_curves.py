import matplotlib.pyplot as plt
import math
import numpy as np

def m_curve(v, mhalf, mk):
    return 1/(1 + math.exp((mhalf - v)/mk))

def h_curve(v, hhalf, hk):
    return 1/(1 + math.exp((hhalf - v)/hk))

def n_curve(v, nhalf, nk):
    return 1/(1+math.exp((nhalf - v)/nk))

def main():
    voltage = np.linspace(-140, 30, 1000)
    m_values = np.asarray([m_curve(v, -40, 10) for v in voltage])
    h_values = np.asarray([h_curve(v, -69, -3.5) for v in voltage])
    n_values = np.asarray([n_curve(v, -53, 15) for v in voltage])


    fig, ax = plt.subplots()
    ax.plot(voltage, m_values, label="m-curve")
    ax.plot(voltage, h_values, label="h-curve")
    ax.plot(voltage, n_values, label="n-curve")

    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()