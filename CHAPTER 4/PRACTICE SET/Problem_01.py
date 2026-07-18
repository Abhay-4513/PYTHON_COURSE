# Write a program to store seven fruits in a list entered by the user

fruits = []

# fruit_1 = input("Enter 1st fruit name : ")
# fruits.append(fruit_1)

# fruit_2 = input("Enter 2nd fruit name : ")
# fruits.append(fruit_2)

# fruit_3 = input("Enter 3rd fruit name : ")
# fruits.append(fruit_3)

# fruit_4 = input("Enter 4th fruit name : ")
# fruits.append(fruit_4)

# fruit_5 = input("Enter 5th fruit name : ")
# fruits.append(fruit_5)

# fruit_6 = input("Enter 6th fruit name : ")
# fruits.append(fruit_6)

# fruit_7 = input("Enter 7th fruit name : ")
# fruits.append(fruit_7)

# print(fruits)

#--------This is the smaller way in which above program can be written-------
for i in range(1,8):
    fruit_name = input("Enter the name : ")
    fruits.append(fruit_name)
print(fruits)
