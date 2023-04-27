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

length = 1000
position_x = [0]*length
position_y = [0]*length


position_x[0] = 0.5
position_y[0] = h

gravity = -9.8
time = []

#Defining the line function of the paddle
x_discrete = np.linspace(1,1.75,100)

angle = 3.14/4
m = 1/(np.tan(angle)) #slope of line (as a function of the angle for simplicity)
line_func = np.array(m*(x_discrete-1))
print(x_discrete.shape)
print(line_func.shape)
x = -1
y = np.tan(angle)
line_func=np.array([])

    
norm_x = x/(np.sqrt(x**2+y**2)) #need unit vector of normal vector to calculate ball reflection
norm_y = y/(np.sqrt(x**2+y**2))
normal_vector = np.array([norm_x,norm_y])
print(normal_vector)

execute = True
dt = 0.01

for i in range(1, length):
     position_y[i] = position_y[i-1] + velocity_y*dt
     position_x[i] = position_x[i-1] + velocity_x*dt
     
     if(position_y[i]-m*(position_x[i]-1) < 0): #check if the ball's coordinates lie on the line
         print("Position x: " +str(position_x[i]) + "  "+"Position y: " + str(position_y[i]))
         print("Velocity x: " +str(velocity_x) + "  "+"Velocity y: " + str(velocity_y))
         
         velocity_vector = np.array([velocity_x,velocity_y])
         velocity_vector = velocity_vector-2*(np.dot(velocity_vector,normal_vector))*normal_vector #Essentially the algrothim for ray tracing
         print(velocity_vector)
         velocity_x = velocity_vector[0]
         velocity_y = velocity_vector[1]

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
   
     
         #break
         
        


         #velocity_x = (2*(velocity_x*norm_x + velocity_y*norm_y)*norm_x - velocity_x)
         #velocity_y = (2*(velocity_x*norm_x + velocity_y*norm_y)*norm_y - velocity_y)    
         
table = np.linspace (0,1,2)
paddle = np.linspace(0,1,2)





#fig, axs = plt.plot

plt.plot(position_x,position_y , label="ball path")
plt.plot(x_discrete, m*(x_discrete-1), label = "Angled Paddle" )
plt.plot(table,[0,0],"-r")
plt.plot([0,0],paddle,"-r")

plt.suptitle('X vs Y distance')
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