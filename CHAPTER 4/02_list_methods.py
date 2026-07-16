# In this i have used some of the common operations on the list...
# There are alot of comments , so don't think this is made using A.I . This is written by a human itself............

names = ["Python","Java","Cybersecurity",35,45]
print(names)

# -----------Append-----------
names.append("Lakh") # Append is used to insert any element in the last of the list..
print(names)

# -----------Sort-----------
number1 = [25,23,24,21,20,22]
number1.sort() # It will sort the given list..
print(number1)

# -----------Reverse-----------
number2 = [10,9,8,7,6,5,4,3,2,1,0]
number2.reverse() # It will print the list from the last number of the actual list
print(number2)

# -----------Pop-----------
number3 = [5,8,4,3,6]
number3.pop(2) # This will remove the element from the selected index...
print(number3.pop(2)) # This will print the poped value
print(number3)

# -----------Remove-----------
names_2 = ["Fury","Tony","Steve","Peter","Scarlet","Banner","Romanova","Balbeer"]
names_2.remove("Balbeer") # This is used to remove and element from the list ...
print(names_2)

# -----------Insert-----------
number2.insert(11,1111) # This is used to insert any element at any index , (index,element)
print(number2)  