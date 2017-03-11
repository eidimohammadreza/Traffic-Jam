# the Car class

class Car(object):
# __init__
    def __init__(self, x, v, min_dist, target_v):
        self.x_ = x;
        self.min_dist_ = min_dist
        self.v_ = v
        self.target_v_ = target_v 

# methods
    @property
    def x(self):
        return self.x_

    @property
    def v(self):
        return self.v_

    def set_v(self, v):
        self.v_ = v


    def update(self, next_car):
        if self.target_v_ * dt < self.min_dist_:
            self.v_ = self.target_v_
        else:
            self.v_ = float(next_car.x - self.min_dist_ - self.x_)/dt

        self.x_ = self.x_ + self.v_ * dt
        

class Street(object):
    def __init__(self):
        self.L = [1,2,3]




# ===== The following lines are for testing how the Car class works =====

t = 1
dt = 0.01
s1 = Street()

c1 = Car(2, 3, 4, 5)
print c1.x

c1.set_v(100)
print c1.v

c2 = Car(5, 6, 7, 8)
c2.x_ = 999
print c2.x

print c1.update(c2) # currently prints None
