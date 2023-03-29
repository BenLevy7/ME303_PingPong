import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib import cm
import numpy as np
from matplotlib import pyplot as plt


paddle_dist = 1
position_x = []
position_y = []
velocity_y = []
time = []


position_x = [0]*10000
position_y = [0]*10000
velocity_y = [0]*10000

velocity_x = 0.1


time = [0]*10000


position_y[0] = paddle_dist/2
#paddle_norm_x = round(np.cos(angle),2)
#paddle_norm_y = round(np.sin(angle),2)


#result_angle_x = -(2*(direction_x*paddle_norm_x + direction_y*paddle_norm_y)*paddle_norm_x - direction_x)
#result_angle_y = (2*(direction_x*paddle_norm_x + direction_y*paddle_norm_y)*paddle_norm_y - direction_y)

increment = 0.01

for i in range(1, 100):
    time[i] = time[i-1] + increment
    velocity_y[i] = velocity_y[i-1] +(9.81)*time[i]

    position_x[i] = position_x[i-1] + velocity_x*time[i]
    position_y[i] = position_y[i-1] + velocity_y[i]*time[i]
    

    
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
