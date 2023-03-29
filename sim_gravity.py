import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib import cm
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import math


paddle_dist = 1
h = 1
position_x = []
position_y = []
velocity_y = []


time = []

position_x = [0]*5000
position_y = [0]*5000
velocity_y = [0]*5000
position_x[0] = 0.5


velocity_x = 0.5


gravity = -9.8



position_y[0] = h

execute = True
paddle_norm_x = -round(np.cos(45),2)
paddle_norm_y = round(np.sin(45),2)



dt = 0.01

for i in range(1, 2000):
     position_y[i] = position_y[i-1] + velocity_y[i-1]*dt
     position_x[i] = position_x[i-1] + velocity_x*dt
   
     if(position_y[i] > 0):
         velocity_y[i] = velocity_y[i-1]+gravity*dt
     else:
         velocity_y[i] = velocity_y[i-1]*-1
   
     if (position_x[i] < 0):
        position_x[i] = 0
        velocity_x*=-1
     #if(paddle_dist-position_x[i] < 0.3 and execute == True and i>100):
        #position_x[i] = 0.9
        #velocity_x*=-1
        #execute = False
         
     if(paddle_dist-position_x[i] < 0):
       
         position_x[i] = 1
         velocity_x*=-1





fig, axs = plt.subplots(2)
axs[0].set_title('X vs Y distance')
axs[0].set_xlabel("X distance")
axs[0].set_ylabel("Y distance ")
axs[0].plot(position_x,position_y , label="ball")

axs[0].legend()
axs[0].legend(loc="lower left")


plt.tight_layout()
plt.show()


# # Animation
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = ax.plot([], [], 'ro')

# def init():
#     ax.set_xlim(-0.1, 0.1)
#     ax.set_ylim(-0.1, 1)
#     return ln,

# def update(frame):
#     xdata.append(frame[0])
#     ydata.append(frame[1])
#     ln.set_data(xdata, ydata)
#     return ln,

# ani = FuncAnimation(fig, update, frames=zip(position_x, position_y),
#                     init_func=init, blit=True)
# plt.show()