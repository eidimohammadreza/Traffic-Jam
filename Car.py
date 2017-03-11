# for testting the Car class

class Car(object):
# __init__
    def __init__(self, x, v, min_dist, target_v, street = "0"):
        self.x_ = x;
        self.min_dist_ = min_dist
        self.v_ = v
        self.target_v_ = target_v
        self.street_ = street

# methods
    @property
    def x(self):
        return self.x_

    @property
    def v(self):
        return self.v_

    def set_v(self, v):
        self.v_ = v

    def set_street(self, street_name):
        self.street_ = street_name

    @property
    def street(self):
        return self.street_

    def update_v(self):
        return s1.L




class Street(object):
    def __init__(self):
        self.L = [1,2,3]





# ===== The following lines are for testing how the Car class works =====

t = 1

s1 = Street()

c1 = Car(2, 3, 4, 5)
print c1.x

c1.set_v(100)
print c1.v

c1.set_street("Azadi")
print c1.street

c2 = Car(5, 6, 7, 8)
c2.x_ = 999
print c2.x

print c1.update_v()
