# Write a Python program to print all names from a list that start with the letter 'S'.

l = ["Harry","Soham","Sachin","Rahul"]

for name in l:
    if name.startswith("S"):
        print(f"Hello {name}")