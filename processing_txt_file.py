from os import strerror

try:
    counter = 0
    stream = open('haming code.py', 'rt', encoding='utf-8') #pytho.txt #receipt.pdf raises error
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1 # for counting char
        char = stream.read(1) # updating char
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


# Reading all at once READ() WITH NO ARGUMENTS
##from os import strerror
##
##try:
##    counter = 0
##    stream = open('C:\\Users\\bened\\Desktop\\PowerShellBeginners\\PSbeginner.ps1', "rt")
##    # stream = open('C:\\Users\\bened\\Desktop\\LearnShellorBash\\hello.sh', "rt") #text.txt
##    content = stream.read()
##    for char in content:
##        print(char, end='')
##        counter += 1
##    stream.close()
##    print("\n\nCharacters in file:", counter)
##except IOError as e:
##    print("I/O error occurred: ", strerr(e.errno))


# READLINE()
##from os import strerror
##
##try:
##    character_counter = line_counter = 0
##    stream = open('text.txt', 'rt')
##    line = stream.readline()
##    while line != '':
##        line_counter += 1
##        for char in line:
##            print(char, end='')
##            character_counter += 1
##        line = stream.readline()
##    stream.close()
##    print("\n\nCharacters in file:", character_counter)
##    print("Lines in file:     ", line_counter)
##except IOError as e:
##    print("I/O error occurred:", strerror(e.errno))

# READLINES()
stream = open("text.txt")
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
stream.close()

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))



##from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))


# DEALING WITH TEXT FILES /WRINTING()
##from os import strerror
##
##try:
##	file = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
##	for i in range(10):
##		s = "line #" + str(i+1) + "\n"
##		for char in s:
##			file.write(char)
##	file.close()
##except IOError as e:
##	print("I/O error occurred: ", strerror(e.errno))


#Can you print the file's contents to the console?

##from os import strerror
##
##try:
##    file = open('newtext.txt', 'wt')
##    for i in range(10):
##        file.write("line #" + str(i+1) + "\n")
##    file.close()
##except IOError as e:
##    print("I/O error occurred: ", strerror(e.errno))
##
##
##import sys
##sys.stderr.write("Error message")


## Bytearray: resemble lists, they are mutable
## important limitation you mustn't set any byte array elements with a value which is not an in
## you're not allowed to assign a value that doesn't come from the range 0 to 255 inclusive
## armophous Data
data = bytearray(200)

for i in range(len(data)):
    data[i] = 200 - i

for b in data:
    print(hex(b))

## how to write a byte array to a binary file
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb') # write binary flag
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.


## 4.3.6 How to read bytes from a stream
from os import strerror

data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


## 4.3.7 Copying files - a simple and functional tool
from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()

## Character frequency histogram
from os import strerror

# Initialize 26 counters for each Latin letter.
# Note: we've used a comprehension to do that.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # If it is a letter...
            if char.isalpha():
                # ... we'll treat it as lower-case and update the appropriate counter.
                counters[char.lower()] += 1
    file.close()
    # Let's output the counters.
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    

##########################################################3
#############3Sorted Histogram for letter count iin a file
from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    file.close()
    file = open(file_name + '.hist', 'wt')
    # Note: we've used a lambda to access the directory's elements and set reverse to get a valid order.
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[char]
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))




try:
    stream = open("image.png", "rb")
    # Insert a line here.
    stream.close()
except IOError:
    print("failed")
else:
    print("success")



# A base exception class for our code:
##4.3.10   LAB   Evaluating students' results
##Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of points the student received during certain classes.
##
##The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.
##
##The file may look as follows:
##
##John     Smith    5
##Anna     Boleyn   4.5
##John     Smith    2
##Anna     Boleyn   11
##Andrew   Cox      1.5
##samplefile.txt
##Your task is to write a program which:
##
##asks the user for Prof. Jekyll's file name;
##reads the file contents and counts the sum of the received points for each student;
##prints a simple (but sorted) report, just like this one:
#Expected outputt
##Andrew   Cox      1.5
##Anna     Boleyn   15.5
##John     Smith    7.0
class StudentsDataException(Exception):
    pass


# An exception for erroneous lines:
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


# An exception for an empty file.
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


from os import strerror

# A dictionary for students' data:
data = { }

file_name = input("Enter student's data filename: ")
line_number = 1
try:
    f = open(file_name, "rt")
    # Read the whole file into list.
    lines = f.readlines()
    f.close()
    # Is the file empty?
    if len(lines) == 0:
        raise FileEmpty()
    # Scan the file line by line.
    for i in range(len(lines)):
        # Get the i'th line.
        line = lines[i]
        # Divide it into columns.
        columns = line.split()
        # There shoule be 3 columns - are they there?
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        # Build a key from student's given name and surname.
        student = columns[0] + ' ' + columns[1]
        # Get points.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        # Update dictionary.
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    # Print results.
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
except WrongLine as e:
    print("Wrong line #" + str(e.line_number) + " in source file:" + e.line_string)
except FileEmpty:
    print("Source file empty")
    
    
    


    
    


    
    
