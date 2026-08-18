n = int(input("Enter the number : "))

sum = 0
for i in range(2,n+1,2):
  print(f"Even number : {i}")
  sum = i + sum

print(f"Sum of even numbers from 2 to {n} is : {sum}")
