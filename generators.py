import sys
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
    

class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(8)

for i in object:
    print(i)
    

def fun(n):
    for i in range(n):
        yield i
 
 
for v in fun(5):
    print(v)
    
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
for v in powers_of_2(8):
    print(v)

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
t = [x for x in powers_of_2(5)]
print(t)


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
for i in range(20):
    if i in powers_of_2(4):
        print(i)

# the fibonnacci in generators
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n
 
fibs = list(fibonacci(10))
print(fibs)

# List comprehensions
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

# comprehensive list
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)

## turn any list comprehension into a generator.
## List comprehensions vs. generators
## It's the parentheses. The brackets make a comprehension, the parentheses
# make a generator.

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()


##Of course, saving either the list or the generator is not necessary –
##you can create them exactly in the place where you need them – just like
##here:


for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print(sys.getsizeof(list))
 
for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print(sys.getsizeof(generator))

## Programmers use the lambda function to simplify the code
## Mathematicians use the Lambda calculus in many formal systems connected with logic,
## recursion, or theorem provability
## A lambda function is a function without a name (you can also call it an anonymous function

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

## lambda has single line
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep=' ')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)
###############Lambda The code has become shorter, clearer, and more legible

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')
 
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

##4.1.7 Lambdas and the map() function
##In the simplest of all possible cases, the map() function:


map(function, list)
 

##takes two arguments:
##
##a function;
##a list. or an entity that can be iterated
## can accept more than 2 args
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()


## filter function
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

##Closures in Python
##Let's analyze a simple example:

def outer(par):
    loc = par
 
 
var = 1
outer(var)
 
print(par)
print(loc)

###Some modifications on the above code
###nonlocal scope var within inner functions

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())
# The function returned during the outer() invocation is a closure.
# inner implementing the idea of encapusulation and data hiding

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

