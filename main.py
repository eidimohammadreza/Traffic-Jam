# main part of Traffic Jam 

import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import animation


import constants
from Car import Car
from Street import Street

def time_to_steps(t):
    return int(t/dt +1)


# taking inputs from the user:
# for testing purposes, I've commented them so not being stuck with typing inputs every time we test the main.py
# hint: a way of getting inputs as argument values should be implemented
# 
"""
v_i = float( input("please enter the initial velocity in term of km/h = ") )
max_cars = int( input("please enter the max number of cars in the street = ") )
dt = float( input("please enter the time step for computation (e.g. 0.1, 0.01, ...) = ") )
total_time = float( input("please enter the total time of simulation (in seconds) = ") )
time_interval = float( input("please enter the time interval for adding new car to street (in seconds) = ") )
"""

t = 0.0
dt = constants.time_step
total_time = 100 # seconds
street_length = 15 # meters
max_cars = 20
#time_interval = 10
generation_step = time_to_steps(1)
max_steps = time_to_steps(total_time)

s = Street(street_length)


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, street_length), ylim=(-2, 2))
line, = ax.plot([], [], 'o', lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

def animate(i):
#    x1 = np.linspace(0, 2, 1000)
#    y1 = np.sin(2 * np.pi * (x1 - 0.01 * i))
#    print x1,y1
       
    



    #print "- step ", i, ":"
    if i%generation_step == 0:
        #later : check if there's no car in the generating point
        target_v = random.uniform(0, 10)
        x, v, min_dist = 0, random.uniform(1, target_v), random.uniform(1,5)
        print "car created with:", x, v, min_dist, target_v, "\n"
        c = Car(x, v, min_dist, target_v)
        s.add_car(c)
    
    x = s.x_list
    y = np.zeros(len(x))  
    #print s.x_list
    #print y
    line.set_data(x, y) 
  

    s.update_cars()




#    t = t + dt
    #s.status_print()
    return line,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, np.arange(0, max_steps),interval=20, blit=False, init_func=init)






plt.show()




