# Write a program to calculate the grade of students from his marks from the following scheme
num1 = int(input("Enter your Maths marks : "))
num2 = int(input("Enter your Physics marks : "))
num3 = int(input("Enter your Python marks : "))

percentage = ((num1+num2+num3)/300)*100
if (percentage<=100 and percentage>=90):
    print("Your grade is : Ex")

elif (percentage<90 and percentage>=80):
    print("Your grade is : A")

elif (percentage<80 and percentage>=70):
    print("Your grade is : B")

elif (percentage<70 and percentage>=60):
    print("Your grade is : C")
    
elif (percentage<60 and percentage>=50):
    print("Your grade is : Y")

elif (percentage<50):
    print("fail")

else:
    print("Enter a valid percentage ")
