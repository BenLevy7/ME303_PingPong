import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
from matplotlib import cm
import numpy as np
from matplotlib import pyplot as plt

# want to iterate through position until wall is hit
paddle_dist = 1
position_x = []
position_y = []
direction_x = 1
direction_y = 0
time = []
velocity = []
# direction_vector = []

position_x = [0]*1000
position_y = [0]*1000
time = [0]*1000


position_x[0] = paddle_dist/2

increment = 0.01

# Angled paddle
angle = np.pi/4

paddle_norm_x = round(np.cos(angle),2)
paddle_norm_y = round(np.sin(angle),2)
print(paddle_norm_x)
print(paddle_norm_y)

result_angle_x = -(2*(direction_x*paddle_norm_x + direction_y*paddle_norm_y)*paddle_norm_x - direction_x)
result_angle_y = -(2*(direction_x*paddle_norm_x + direction_y*paddle_norm_y)*paddle_norm_y - direction_y)
print(result_angle_x)

for i in range(1, 1000):

    position_x[i] = round(position_x[i-1]+increment*direction_x, 5)
    position_y[i] = round(position_y[i-1]+increment*direction_y, 5)

    # print(position_x[i])

    if (position_x[i] == abs(paddle_dist)) or position_x[i] == 0:
        if (i == 10):
            direction_x = result_angle_x
            direction_y = result_angle_y
        else:

            direction_x *= -1

   # print(direction_x)
    time[i] = time[i-1] + increment
    # print(time[i])

fig, axs = plt.subplots(2)
axs[0].set_title('X vs Y distance')
axs[0].set_xlabel("X distance")
axs[0].set_ylabel("Y distance ")
axs[0].plot(position_x, position_y, label="ball")

axs[0].legend()
axs[0].legend(loc="lower left")

axs[1].set_title('X distance over time')
axs[1].set_xlabel("X")
axs[1].set_ylabel("Y")
axs[1].plot(time, position_x, label="ball")

axs[1].legend()
axs[1].legend(loc="lower left")

plt.tight_layout()
plt.show()
