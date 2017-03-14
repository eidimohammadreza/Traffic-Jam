# the Car class
import constants, random
dt = constants.time_step


def prob(p):
    a = random.uniform(0,1)
    if a<p:
        return True
    else:
        return False


class Car(object):
# __init__
    def __init__(self, x, v, min_dist, target_v, stop = False):
        self.x_ = x
        self.min_dist_ = min_dist
        self.v_ = v
        self.target_v_ = target_v

        self.stop_ = stop
# status
    def __str__(self): # just for printing a car's status directly
        status = "x: {} ,   v: {}   ,   min dist:   {}  ,   target v:   {}\n"
        return status.format(self.x_, self.v_, self.min_dist_, self.target_v_)
    def status(self): # returns the status as a list, useful when running Street's status function
        return [self.x_, self.v_, self.min_dist_, self.target_v_]

# methods
    @property
    def x(self):
        return self.x_

    @property
    def v(self):
        return self.v_
    @property
    def min_dist(self):
        return self.min_dist_

    def set_v(self, v):
        self.v_ = v


    def update(self, next_car = None): # for a completely rational driver

        if next_car == None:
            self.v_ = self.target_v_
        else:
            self.v_ = min( self.target_v_, float(next_car.x - self.min_dist_ - self.x_)/dt )
            # here we assume that the front car is moved before; but even if it
            # hasn't, we take the worst case in which we assume the fron car's
            # velocity will be set to 0, and that again results the same equation.
        if self.stop_ == True:
            self.v_ = 0
        """
        if(prob(0.05)):
            self.v_ = 0
        """

        self.x_ = self.x_ + self.v_ * dt


# ===== The following lines are for testing how the Car class works =====
#dt = 0.01 # should be here! solve it later

"""
t = 0.0
dt = 0.1

c1 = Car(2.0, 0.3, 0.4, 15.0)
#print c1.target_v_
c2 = Car(0.15,0.1, 0.04, 16.0)
#print c2.target_v_


for i in range(25):
    c1.update()
    print "C1 -->", c1.x, c1.v
    c2.update(c1)
    print "C2 -->", c2.x, c2.v
    if i == 20:
        c1.set_v(0)
    print " -------------------------------------", c1.x , c2.x, "------------------------------------------"

    print "\n"
"""


