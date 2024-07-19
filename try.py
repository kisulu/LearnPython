##class Vowels:
##    def __init__(self):
##        self.vow = "aeiouy " # Yes, we know that y is not always considered a vowel.
##        self.pos = 0
## 
##    def __iter__(self):
##        return self
## 
##    def __next__(self):
##        if self.pos == len(self.vow):
##            raise StopIteration
##        self.pos += 1
##        return self.vow[self.pos - 1]
##
##list(map(lambda n: n | 1, any_list))
## 
## 
##vowels = Vowels()
##for v in vowels:
##    print(v, end=' ')
##
##def replace_spaces(replacement='*'):
##    def new_replacement(text):
##        return text.replace(' ', replacement)
##    return new_replacement
## 
## 
##stars = replace_spaces()
##print(stars("And Now for Something Completely Different"))

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

class stack:
    def __init__(self):
        self.mylist = []
        for x in range(10):
            self.mylist.append(x**2)
            
    def push(self, x):
        self.x=x
        if x > 10:
            self.mylist.append(x)
            print(self.mylist)

    def pop(self):
        self.mylist.pop()
        print(self.mylist)

stackobj = stack()
stackobj.push(11)
stackobj.pop()

import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
        
