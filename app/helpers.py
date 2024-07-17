import matplotlib.pyplot as plt
import numpy as np

def moduladora(scale, t):
    return scale*t



def accel_frequency(scale, semi_cicles, points):
    T = np.sqrt(semi_cicles/(2*scale))
    x = np.linspace(0, T, points)
    y = np.array([np.sin(2*np.pi*moduladora(scale, tau)*tau) for tau in x])
    return x, y
    

