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


time = 0
length = 4000

position_x = [0]*length 
position_y = [0]*length 
velocity_y = [0]*length 
position_x[0] = 0


velocity_x = 11.76


gravity = -9.8



position_y[0] = h


dt = 0.01

for i in range(1, length ):
     position_y[i] = position_y[i-1] + velocity_y[i-1]*dt
     position_x[i] = position_x[i-1] + velocity_x*dt
   
   
     if(position_y[i] > 0):
         velocity_y[i] = velocity_y[i-1]+gravity*dt
     else:
         
         velocity_y[i] = velocity_y[i-1]*-1
         #position_y[i] = 0
   
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
     time+=dt

#setting up paddle and table
table = np.linspace (0,1,2)
paddle = np.linspace(0,1,2)

print("Time = "+str(time))


plt.plot(position_x,position_y , label="ball path")
plt.scatter(position_x[0],h,color = 'black', label ="Starting position ")
plt.plot(table,[0,0],"-r")
plt.plot([0,0],paddle,"-r")
plt.plot([1,1],paddle,"-r")
plt.suptitle('X vs Y distance (40 Second Duration)')
plt.xlabel("X distance")
plt.ylabel("Y distance ")
plt.legend()
plt.legend(loc="lower left")


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