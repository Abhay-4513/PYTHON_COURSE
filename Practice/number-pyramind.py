# Write a program to print a number triangle (row i contains numbers 1 to i).

n = int(input("Enter the number : "))

for i in range(1,n+1):
    print(f" "*(n-i), f"{i} "*i)