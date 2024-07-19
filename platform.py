#!/usr/bin/env python3
"""module.py - an example of a Python module """ #doc sting
from platform import platform
from platform import machine
from platform import processor
from platform import system
from platform import version
from platform import python_implementation, python_version_tuple
import os
import sys

if __name__ == "__main__":
    print(__name__)
    print(dir(os))
    print(python_implementation())

    for atr in python_version_tuple():
        print(atr)

     
    print(version())
     
    print(system())

     
     
    print(processor())
     
    print(machine())

    print(platform())
    print(platform(1))
    print(platform(0, 1))

    import math
    result = math.e == math.exp(1)
    print(result)

    counter = 0
       
else:
   print("I like to be a module.")


__counter = 0
 
 
def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum

def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod
 
 
if __name__ == "__main__":
  print("I prefer to be a module, but I can do some tests for you.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)

for p in sys.path:
    print(p)

##from sys import path
## 
##path.append('..∖∖modules')
## 
##import module
##
##
##from sys import path
## 
##path.append('..∖∖packages∖∖extrapack.zip')
## 
##import extra.good.best.sigma as sig
##import extra.good.alpha as alp
##from extra.iota import funI
##from extra.good.beta import funB
## 
##print(sig.funS())
##print(alp.funA())
##print(funI())
##print(funB())
