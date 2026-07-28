# Write a program which finds out whether a given name is peresent in list or not 

List = ["abhay","tony","banner","steve","sam","natasha","thor"]

user = input("Enter you name to check if you are avenger or not : ")

if ((user.lower()) in List):
    print("You are avenger...")
else:
    print("Maybe in next life -_-")