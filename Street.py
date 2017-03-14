from Car import Car
class Street(object):
# __init__
    def __init__(self, length, cars = [], lines = 1):
        self.length_ = float(length)
        self.cars_ = cars
        self.lines_ = lines

        # new! this is for queueing the entrance of new cars
        self.queue_ = []

# status
    def status_print(self):
        print "\n===== Status of street: =====\n"
        for car in self.cars_:
            print car

    def status_list(self):
        status_list =[]
        for car in self.cars_:
            status_list.append( car.status() )
        return status_list

# methods
    @property
    def length(self):
        return self.length_

    @property
    def cars(self):
        return self.cars_

    @property
    def lines(self):
        return self.lines_

    @property
    def x_list(self):
        X = []
        for car in self.cars_:
            X.append(car.x)
        return X

    @property
    def v_list(self):
        v = []
        for car in self.cars_:
            v.append(car.v)
        return v


    def add_car(self, c):
        if len(self.cars_) > 0:
            if len(self.queue_) > 0:
                self.queue_.append(c)
                print ">> added a car to queue"
            else:
                nearest_car = self.cars_[-1]
                if abs(nearest_car.x - c.x) > c.min_dist:
                    self.cars_.append(c)
                else:
                    self.queue_.append(c)
                    print ">> added a car to queue"
        else:
            self.cars_.append(c)

    def update_cars(self):

        # Notice! : the first item in the list is the last car in the street queue
        for i in range( 1, len(self.cars_) ): # now update other cars behind it, respectively
            car = self.cars_[-i]
            next_car = self.cars_[-1-i]
            car.update(next_car)
        end_car = self.cars_[0]
        end_car.update()
        if len(self.queue_) > 0:
            first_in_queue = self.queue_[0]
            nearest_car = self.cars_[-1]
            if nearest_car.x > first_in_queue.min_dist:
                self.cars_.append(first_in_queue)
                del self.queue_[0] #after adding it, remove it from queue
                print "<< car entered to the street from the queue"

"""
s = Street(100)
c1 = Car(10,2,3,4)
c2 = Car(5,6,7,8)
c3 = Car(0, 1, 5, 7)
s.add_car(c1)
s.add_car(c2)
print len(s.cars_)
s.update_cars()
s.status_print()
s.update_cars()
s.status_print()
s.update_cars()
s.status_print()
s.update_cars()
s.status_print()
s.add_car(c3)
s.status_print()
print s.x_list
"""

