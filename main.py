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
total_time = 200 # seconds
street_length = 200 # meters
max_cars = 20
#time_interval = 10
generation_step = time_to_steps(1)
max_steps = time_to_steps(total_time)

s = Street(street_length)


# First set up the figure, the axis, and the plot element we want to animate

fig = plt.figure()


ax1 = fig.add_subplot(211, autoscale_on=False, xlim=
(0, street_length), ylim=(-2, 2))
#ax1.grid()
ax1.set_title('Traffic Jam')


ax1.plot((0,street_length),(0.5,0.5),c='black')
ax1.plot((0,street_length),(-0.5,-0.5),c='black')
ax1.set_yticks([])

ax2 =fig.add_subplot(212, autoscale_on=False, xlim=(0, street_length), ylim=(0, 50))
ax2.set_ylabel('Time (s)')
ax2.set_xlabel('Cars Positions (m)')



#Animate the cars
line1, = ax1.plot([], [], marker='s',lw=0,markersize=3)

#Create a list that stores the plot for each cars history
lines = []



# initialization function: plot the background of each frame
def init():
    line1.set_data([], [])
    return line1    

def animate(i):


    #Checks if should generate a new car:
   
    #print "- step ", i, ":"
    if i%generation_step == 0:
        #later : check if there's no car in the generating point
        target_v = random.uniform(10, 10)
        x, v, min_dist = 0, random.uniform(1, target_v), random.uniform(1,5)
        print "car created with:", x, v, min_dist, target_v, "\n"
        c = Car(x, v, min_dist, target_v)
        s.add_car(c)
        lines.append(ax2.plot([], [], '-', lw=1)[0])
    
    #sets time and gets the position of each car. y position is set to zero by default.
    t=i*dt
    x = s.x_list
    y = np.zeros(len(x)) 
    
    
    #updates the position of each car in the graph.
    line1.set_data(x,y)

    #stores the history of each car in its correspondant plot.
    j=0
    for linita in lines:
        
        
        linita.set_xdata(np.append(linita.get_xdata(),x[j]))
        linita.set_ydata(np.append(linita.get_ydata(),t))
        j=j+1

  
    #calls the function that updates the position of the cars
    s.update_cars()

    return line1, lines




# call the animator.  blit=True means only re-draw the parts that have changed.

anim = animation.FuncAnimation(fig, animate, np.arange(0, max_steps),interval=20, blit=False, init_func=init)


plt.show()




