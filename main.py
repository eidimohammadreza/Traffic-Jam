# main part of Traffic Jam 


import numpy as np
import matplotlib.pyplot as pl
import random

#import street
import Car


vi=float(input("please enter the initial velocity in term of km/h = "))
nm=int(input("please enter the max number of cars in the street = "))
dt=float(input("please enter the time step for computation (e.g. 0.1, 0.01, ...) = "))
tt=float(input("please enter the total time of simulation (in term of min) = "))
ti=float(input("please enter the time interval for adding new car to street (in term of Sec) =  "))

tt*=60

st=[]   # creation of street
tv=[]

# creation of target of velecities

for i in range (nm+1):
    tv=random.uniform(2*vi,10*vi)
    

for t in range (0,tt,dt) :
    if t % ti == 0:
        st.append(t)
    

