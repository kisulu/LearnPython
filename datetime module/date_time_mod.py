from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

## Creating a Date Object
from datetime import date

my_date = date(2019, 11, 4)
print(my_date)


## Note: Later in this course you'll learn how to change the default date format.
## UNIX epoch
## Creating objects from timestamp
## time(), which returns the number of seconds from January 1, 1970 to the current moment 
from datetime import date
import time

## time in seconds sin January 1, 1970
timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

## 4.5.4 Creating a date object using the ISO format
## ISO 8601 standard, fromisoformat method, takes a date in the YYYY-MM-DD

## Replace method
from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

## 4.5.6 What day of the week is it?
from datetime import date

d = date(2024, 7, 21)
print(d.weekday())


## isodayweek method follows the ISO 85601 specification
 
d = date(2019, 11, 4)
print(d.isoweekday())

## Time Object from time class in datetime module
from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)

#Time module
import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)

## 4.5.10 The gmtime() and localtime() functions
## time module require knowledge of the struct_time class
import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

## 4.5.11 The asctime() and mktime() functions
    
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

## 4.5.12 Creating datetime objects
## 4.5.13 Methods that return the current date and time
from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())

## 4.5.14 Getting a timestamp
## The timestamp method returns a float value expressing the number of seconds elapsed between the date and time indicated by the
## atetime object and January 1, 1970, 00:00:00 (UTC).
from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

## 4.5.15 Date and time formatting
## A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter.
## the separator character can be replaced by another characte
## / (slash)
## %S returns the second as a zero-padded

from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))


from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))
    
    
    
    
    
