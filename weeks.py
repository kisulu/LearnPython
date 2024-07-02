# As you already know, an object is an incarnation of a class. This means that the object is like a cake baked using a recipe which is included inside the class.
class WeekDayError(Exception):
    pass

class Weeker:
    x=int(input("type any number: "))
    def __init__(self):
        self.day=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def day_in_week(self):
        if Weeker.x > 6 or Weeker.x < 0:
##            if Weeker.x != 0:
                print("only seven days in a week")
        else:
            for d in self.day:
                d = self.day[Weeker.x]
            print(d)
            
##        x =int(input("type any number: "))
##        return self.day_in_week()
            
        
try:        
    obj_day = Weeker(10)
except TypeError:
    obj_day = Weeker()
    obj_day.day_in_week()
    print("Sorry, I can't serve your request.")
except WeekDayError:
    pass

    





	

##class Weeker:
##    #
##    # Write code here.
##    #
##
##    def __init__(self, day):
##        #
##        # Write code here.
##        #
##
##    def __str__(self):
##        #
##        # Write code here.
##        #
##
##    def add_days(self, n):
##        #
##        # Write code here.
##        #
##
##    def subtract_days(self, n):
##        #
##        # Write code here.
##        #
##
##
##try:
##    weekday = Weeker('Mon')
##    print(weekday)
##    weekday.add_days(15)
##    print(weekday)
##    weekday.subtract_days(23)
##    print(weekday)
##    weekday = Weeker('Monday')
##except WeekDayError:
##    print("Sorry, I can't serve your request.")

class Weeker:
    __names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current]

    def add_days(self, n):
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n):
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
    
##
##class Star:
##    def __init__(self, name, galaxy):
##        self.name = name
##        self.galaxy = galaxy
##
##    def __str__(self):
##        # built in cutomize object and return it as a string
##        return self.name + ' in ' + self.galaxy
##
##
##sun = Star("Sun", "Milky Way")
##print(sun) # since previous returns urgle object


# inheritance relation is fully transitive
# if B is a Subclass of A and C is a subclass of B the C is also a subclass of A
