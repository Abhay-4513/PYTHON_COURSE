# A spam comment is defined as a text containing following keywords:
# "Make a lot of money" , "buy now" , "subscribe this" , "click this" . Write a program to detect these messages

p1 = "make a lot of money"
p2 = "buy now" 
p3 = "subscribe this"
p4 = "click this"

usermail = input("Enter your message : ")

if ((p1 in usermail) or (p2 in usermail) or (p3 in usermail) or (p4 in usermail)):
    print("This is spam")

else:
    print("This is not a spam")