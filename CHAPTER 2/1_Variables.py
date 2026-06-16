# Write a python program to print the contents of directory using the os module .

import os

#Specify the directory path 
directory_path = input("Enter the path : ")

# List all the files
contents = os.listdir(directory_path)

# Print each file and directory name...
for item in contents:
    print(item)
