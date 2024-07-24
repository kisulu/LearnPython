import os

try:
    os.makedirs("my_first_directory/my_second_directory")
    os.chdir("my_first_directory")
    
except FileExistsError:
    print("Cannot create a file when that file already exists: 'my_first_directory'")
finally:
    print(os.listdir())

# getting currrent working directory
import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())

# Deleting directories
import os

os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())

# Removes all
import os
 
os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())


# The system function
import os

returned_value = os.system("mkdir my_first_directory")
print(returned_value)
    
