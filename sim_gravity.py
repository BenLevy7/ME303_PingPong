import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib import cm
import numpy as np
from matplotlib import pyplot as plt
import math


paddle_dist = 1
h = 1
position_x = []
position_y = []
velocity_y = []
time = []

position_x = [0]*100
position_y = [0]*100
velocity_y = [0]*100


velocity_x = 0.5
counter_y = 0


time = [0]*100


position_y[0] = h
# paddle_norm_x = round(np.cos(angle),2)
# paddle_norm_y = round(np.sin(angle),2)


# result_angle_x = -(2*(direction_x*paddle_norm_x + direction_y*paddle_norm_y)*paddle_norm_x - direction_x)
# result_angle_y = (2*(direction_x*paddle_norm_x + direction_y*paddle_norm_y)*paddle_norm_y - direction_y)

increment = 0.01
for i in range(1, 100):
     
     time[i] = time[i-1] + increment
    # velocity_y[i] = velocity_y[i-1] - (100)*time[i]

     position_x[i] = position_x[i-1] + velocity_x*time[i]
     
    # position_y[i] = position_y[i-1] + velocity_y[i]*time[i]
    # counter_y+=1

    # if (i>3):
    
     velocity_y[i] = math.sqrt(2*9.8*(1-h))*numpy.sign(velocity_y[i])
     position_y[i] = position_y[i-1] -velocity_y[i]*time[i]
     h-=increment

     if(position_y[i] < 0):
        position_y[i] = 0
        velocity_y[i]*=-1
        increment*=-1
     if(position_y[i] > 1 and i!=1):
        position_y[i] = h
        velocity_y[i]*=-1
        increment*=-1
    
     if (position_x[i] < 0):
        position_x[i] = 0
        velocity_x*=-1
     if(paddle_dist-position_x[i] < 0):
        position_x[i] = 1
        velocity_x*=-1
         
     

        
    



     print(position_y[i])



fig, axs = plt.subplots(2)
axs[0].set_title('X vs Y distance')
axs[0].set_xlabel("X distance")
axs[0].set_ylabel("Y distance ")
axs[0].plot(position_x, position_y, label="ball")

axs[0].legend()
axs[0].legend(loc="lower left")


plt.tight_layout()
plt.show()
