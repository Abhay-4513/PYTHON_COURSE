#This program will the output of this series : 1^2 + 2^2 + 3^2 + ... + n^2.
n = int(input("Enter the number : "))

for i in range(1,n+1):
  print(f"Square of {i} is = {i*i}")
