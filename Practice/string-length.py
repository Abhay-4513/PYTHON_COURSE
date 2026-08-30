# Write a program to find the length of a string without using the built-in len() function.

string = input("Enter a word: ")

length = 0

for i in string:
    length +=1

print(f"The length of the string is: {length}")