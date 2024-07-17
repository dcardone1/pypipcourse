
from helpers import accel_frequency
import matplotlib.pyplot as plt


if __name__=='__main__':
    x, y = accel_frequency(100, 50, 1000)
    plt.plot(x,y)
    plt.savefig('plot_freq')