# Write a program to find whether a given username contain less than 10 characters or not..

usr = input("Enter your name : ")

length = (len(usr))

if(length <10):
    print("Username contain less than 10 characters..")
    print(length)
else:
    print("Username contain more than 10 characters...")
