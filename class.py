class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")

##    def doanything(self): prints the same thing
##        self.do_it()


one = One()
two = Two()

one.doanything()
two.doanything()

##################Generalization and Specification##############
import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(left, stop): # instatiates change direction its more concrete
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)
"""
## change_direction(); note: the former method is empty, as we are going to put
## all the details into the subclass (such a method is often called an abstract method,
##as it only demonstrates some possibility which will be instantiated later)


##The most important advantage (omitting readability issues) is that this form of code enables you to
##implement a brand new turning algorithm just by modifying the turn() method, which can be done in
##just one place, as all the vehicles will obey it.
##
##This is how polymorphism helps the developer to keep the code clean and consistent


##Composition is the process of composing an object using other different objects

#Inheritance is not the only way to construct adaptable classes. You can achieve the same goals (not always, but very often) by using a technique named composition.

inheritance extends a class's capabilities by adding new components and modifying existing ones; in other words, the complete recipe is contained inside the class itself and all its ancestors; the object takes all the class's belongings and makes use of them;
composition projects a class as a container able to store and use other objects (derived from other classes) where each of the objects implements a part of a desired class's behavior.


3.5.7 Single inheritance vs. multiple inheritance
As you already know, there are no obstacles to using multiple inheritance in Python. You can derive any new class from more than one previously defined classes.

There is only one "but". The fact that you can do it does not mean you have to.

Don't forget that:

a single inheritance class is always simpler, safer, and easier to understand and maintain;

multiple inheritance is always risky, as you have many more opportunities to make a mistake in identifying these parts of the superclasses which will effectively influence the new class;

multiple inheritance may make overriding extremely tricky; moreover, using the super() function becomes ambiguous;

multiple inheritance violates the single responsibility principle (more details here: https://en.wikipedia.org/wiki/Single_responsibility_principle) as it makes a new class of two (or more) classes that know nothing about each other;

we strongly suggest multiple inheritance as the last of all possible solutions – if you really need the many different functionalities offered by different classes, composition may be a better alternative.


"""

import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
