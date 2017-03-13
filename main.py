# main part of Traffic Jam 

import numpy as np
import matplotlib.pyplot as pl
import random

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
dt = 0.1
total_time = 100 # seconds
sreet_length = 10000 # meters
max_cars = 20
#time_interval = 10
generation_step = time_to_steps(1)
max_steps = time_to_steps(total_time)

s = Street(sreet_length)


for i in range(max_steps):
    print "- step ", i, ":"
    if i%generation_step == 0:
        #later : check if there's no car in the generating point
        target_v = random.uniform(0, 10)
        x, v, min_dist = 0, random.uniform(0, target_v), random.uniform(0,5)
        print "car created with:", x, v, min_dist, target_v, "\n"
        c = Car(x, v, min_dist, target_v)
        s.add_car(c)
        
    s.update_cars()
    t = t + dt
    s.status_print()




"""
st=[]   # creation of street
tv=[]

# creation of target of velecities

for i in range (nm+1):
    tv=random.uniform(2*vi,10*vi)
    

for t in range (0,tt,dt) :
    if t % ti == 0:
        st.append(t)
"""

