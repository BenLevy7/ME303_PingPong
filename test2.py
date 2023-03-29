import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib import cm
import numpy as np
from matplotlib import pyplot as plt
import math




g = -9.81
y = 0.0
v = 0.0

t = 0
dt = 0.01
y_floor = -5
data = []

while t < 100:
    y += v*dt
    if y > y_floor:
        v += g*dt
    else:
        v = -v   # bounce off floor
    data.append([t, y, v]) 
    t += dt

data = np.array(data) 
data = data.transpose()

plt.plot(data[0], data[1])
plt.xlabel("time (s)")
plt.ylabel("position (m)");
plt.show()