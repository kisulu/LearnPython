class Classy:
    def __init__(self):
        self.visible()
        print("My contructor")
        
    def visible(self):
        print("visible")
 
    def __hidden(self):
        self.__var=10
        print("hidden")
 
 
obj = Classy()
obj.visible()
 
try:
    obj.__hidden()
except:
    print("failed")

if __name__ == "__main__":
    obj._Classy__hidden()
    print(obj._Classy__var)
    print(obj.__dict__)
    print(Classy.__dict__)


class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

class Sample:
    def __init__(self):
        self.name = Sample.__name__
    def myself(self):
        print("My name is " + self.name + " living in a " + Sample.__module__)


obj = Sample()
obj.myself()

# Note: a class without explicit superclasses points to
# an object (a predefined Python class) as its direct ancestor.

# 3.4.3 Reflection and introspection

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

##3.4.6 SECTION QUIZ
##Question 1: The declaration of the Snake class is given below. Enrich the class with a method named increment(), adding 1 to the victims property.
##
##class Snake:
##    def __init__(self):
##        self.victims = 0
##Hide
##class Snake:
##    def __init__(self):
##        self.victims = 0
##
##    def increment(self):
##        self.victims += 1
##
##
##Question 2: Redefine the Snake class constructor so that is has a parameter to initialize the victims field with a value passed to the object during construction.
##
##Hide
##class Snake:
##    def __init__(self, victims):
##        self.victims = victims
##Question 3: Can you predict the output of the following code?
##
##class Snake:
##    pass
## 
## 
##class Python(Snake):
##    pass
## 
## 
##print(Python.__name__, 'is a', Snake.__name__)
##print(Python.__bases__[0].__name__, 'can be', Python.__name__)

def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return two_digits(self.__hours) + ":" + \
               two_digits(self.__minutes) + ":" + \
               two_digits(self.__seconds)

    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

##3.4.8   LAB   Days of the week
##Your task is to implement a class called Weeker. Yes, your eyes don't deceive you – this name comes from the fact that objects of that class will be able to store and to manipulate the days of the week.
##
##The class constructor accepts one argument – a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:
##
##Mon Tue Wed Thu Fri Sat Sun
##
##Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:
##
##objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
##the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
##all object's properties should be private;
##Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.
##
##Expected output
##Mon
##Tue
##Sun
##Sorry, I can't serve your request.

class Weeker:
    def __init__(self, day=[]):
        self.day=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def day_in_week(self):
        self.day=day
        self.x=int(input("type any number: "))
        for self.x in day:
            print(self.x)
        
try:        
    obj_day = (day)
except WeekDayError:
    print("there are only 7 days of the week")
        

import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def distance_from_xy(self, x, y):
        dx = self._x - x
        dy = self._y - y
        return math.hypot(dx, dy)

    def distance_from_point(self, other_point):
        dx = self._x - other_point.getx()
        dy = self._y - other_point.gety()
        return math.hypot(dx, dy)

# Example usage
point1 = Point(1.0, 1.0)
point2 = Point(2.0, 2.0)

distance1 = point1.distance_from_xy(2.0, 2.0)
distance2 = point1.distance_from_point(point2)

print(distance1)  # Expected output: 1.4142135623730951
print(distance2)  # Expected output: 1.4142135623730951

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        #
        # Write code here
        #

    def getx(self):
        #
        # Write code here
        #

    def gety(self):
        #
        # Write code here
        #

    def distance_from_xy(self, x, y):
        #
        # Write code here
        #

    def distance_from_point(self, point):
        #
        # Write code here
        #


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
    

##3.4.9   LAB   Points on a plane
##Let's visit a very special place – a plane with the Cartesian coordinate system (you can learn more about this concept here: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).
##
##Each point located on the plane can be described as a pair of coordinates customarily called x and y. We want you to write a Python class which stores both coordinates as float numbers. Moreover, we want the objects of this class to evaluate the distances between any of the two points situated on the plane.
##
##The task is rather easy if you employ the function named hypot() (available through the math module) which evaluates the length of the hypotenuse of a right triangle (more details here: https://en.wikipedia.org/wiki/Hypotenuse) and here: https://docs.python.org/3.7/library/math.html#trigonometric-functions.
##
##This is how we imagine the class:
##
##it's called Point;
##its constructor accepts two arguments (x and y respectively), both of which default to zero;
##all the properties should be private;
##the class contains two parameterless methods called getx() and gety(), which return each of the two coordinates (the coordinates are stored privately, so they cannot be accessed directly from within the object);
##the class provides a method called distance_from_xy(x,y), which calculates and returns the distance between the point stored inside the object and the other point given as a pair of floats;
##the class provides a method called distance_from_point(point), which calculates the distance (like the previous method), but the other point's location is given as another Point class object;
##Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.
##
##Expected output
##1.4142135623730951
##1.4142135623730951

import math


class Point:
    #
    # The code copied from the previous lab.
    #


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        #
        # Write code here
        #

    def perimeter(self):
        #
        # Write code here
        #


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

##3.4.10   LAB   Triangle
##Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?
##
##The new class will be called Triangle and this is what we want:
##
##the constructor accepts three arguments – all of them are objects of the Point class;
##the points are stored inside the object as a private list;
##the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is the sum of all the lengths of the legs (we mention this for the record, although we are sure that you know it perfectly yourself.)
##Complete the template we've provided in the editor. Run your code and check whether the evaluated perimeter is the same as ours.
##
##Below you can copy the Point class code we used in the previous lab:
    
 
