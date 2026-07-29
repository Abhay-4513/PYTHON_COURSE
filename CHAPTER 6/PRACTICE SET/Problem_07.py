# Write a program to find out whether a give post is talking about "Abhay" or not.

nn = "abhay"
text = input("Enter you message")

if (nn in (text.lower()) ):
    print("It is takling about harry.")
else:
    print("No this is not")
