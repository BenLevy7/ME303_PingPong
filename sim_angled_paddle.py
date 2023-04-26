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
velocity_x = 0.2
position_y = []
velocity_y = 0

position_x = [0]*1000
position_y = [0]*1000


position_x[0] = 0.5
position_y[0] = h

gravity = -9.8
time = []

#Defining the line function of the paddle
angle = 0.17
m = 1/(np.tan(angle)) #slope of line (as a function of the angle for simplicity)
x = -1
y = np.tan(angle)
norm_x = x/(np.sqrt(x**2+y**2)) #need unit vector of normal vector to calculate ball reflection
norm_y = y/(np.sqrt(x**2+y**2))
normal_vector = np.array([norm_x,norm_y])
print(normal_vector)

execute = True
dt = 0.01

for i in range(1, 500):
     position_y[i] = position_y[i-1] + velocity_y*dt
     position_x[i] = position_x[i-1] + velocity_x*dt
   
     if(position_y[i] >= 0):
         velocity_y = velocity_y+gravity*dt
     else:
         velocity_y = velocity_y*-1
   
     if (position_x[i] < 0):
        position_x[i] = 0
        velocity_x*=-1
     #if(paddle_dist-position_x[i] < 0.3 and execute == True and i>100):
        #position_x[i] = 0.9
        #velocity_x*=-1
        #execute = False
   
     if(position_y[i]-m*(position_x[i]-1)  <0.001): #check if the ball's coordinates lie on the line
         print("Position x: " +str(position_x[i]) + "  "+"Position y: " + str(position_y[i]))
         print("Velocity x: " +str(velocity_x) + "  "+"Velocity y: " + str(velocity_y))
         velocity_vector = np.array([velocity_x,velocity_y])
         velocity_vector = velocity_vector-2*(np.dot(velocity_vector,normal_vector))*normal_vector
         print(velocity_vector)
         velocity_x = velocity_vector[0]
         velocity_y = velocity_vector[1]
         #break
         
        


         #velocity_x = (2*(velocity_x*norm_x + velocity_y*norm_y)*norm_x - velocity_x)
         #velocity_y = (2*(velocity_x*norm_x + velocity_y*norm_y)*norm_y - velocity_y)    
         

      





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