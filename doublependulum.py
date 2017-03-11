# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

from numpy import sin, cos, pi, array
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G =  9.8 # acceleration due to gravity, in m/s^2
L1 = 1.0 # length of pendulum 1 in m
L2 = 1.0 # length of pendulum 2 in m
M1 = 1.0 # mass of pendulum 1 in kg
M2 = 1.0 # mass of pendulum 2 in kg



def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2]-state[0]
    den1 = (M1+M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_)
               + M2*G*sin(state[2])*cos(del_) + M2*L2*state[3]*state[3]*sin(del_)
               - (M1+M2)*G*sin(state[0]))/den1

    dydx[2] = state[3]

    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_)
               + (M1+M2)*G*sin(state[0])*cos(del_)
               - (M1+M2)*L1*state[1]*state[1]*sin(del_)
               - (M1+M2)*G*sin(state[2]))/den2

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0.0, 20, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

rad = pi/180

# initial state
state = np.array([th1, w1, th2, w2])*pi/180.

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:,0])
y1 = -L1*cos(y[:,0])

x2 = L2*sin(y[:,2]) + x1
y2 = -L2*cos(y[:,2]) + y1

fig = plt.figure()
ax1 = fig.add_subplot(211, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax1.grid()

ax2 =fig.add_subplot(212, autoscale_on=False, xlim=(-2, 2), ylim=(0, 20))

line, = ax1.plot([], [], 'o-', lw=2)
sb, = ax2.plot([], [], lw=2)
fb, = ax2.plot([], [], lw=2)

time_template = 'time = %.1fs'
time_text = ax1.text(0.05, 0.9, '', transform=ax1.transAxes)

def init():
    line.set_data([], [])
    sb.set_data([], [])
    fb.set_data([], [])
    time_text.set_text('')
    return line, time_text


#def update_line(sb, new_data):
#    sb.set_xdata(numpy.append(sb.get_xdata(), x1))
#    sb.set_ydata(numpy.append(sb.get_ydata(), y1))
#    ax2.draw()

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    time_text.set_text(time_template%(i*dt))
    line.set_data(thisx, thisy)
    print thisx
    #print sb.get_xdata()
    sb.set_xdata(np.append(sb.get_xdata(), thisx[2]))
    sb.set_ydata(np.append(sb.get_ydata(), i*dt))
    fb.set_xdata(np.append(fb.get_xdata(), thisx[1]))
    fb.set_ydata(np.append(fb.get_ydata(), i*dt))
    
    return line, sb, fb, time_text
print np.arange(1,len(y))






fig.ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),interval=50, blit=True, init_func=init)



#ax2.ani = animation.FuncAnimation(fig, update_line, np.arange(1, len(y)),interval=50, blit=True, init_func=init)

#prueba=np.linspace(-np.pi, np.pi, num=50)
#ax2.plot(prueba,np.sin(prueba))
#ax2.grid()






#ani.save('double_pendulum.mp4', fps=15)
plt.show()
