# Write a program to count how many numbers from 1 to n are divisible by 3.

n = int(input("Enter the nth number : " ))
count = 0
a = []
for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1
        a.append(i)
print("The count of numbers from 1 to", n, "divisible by 3 is:", count)
print(f"The list of number are : {a}")