# This program will give the factors which are perfect divisors of the given number.
n = int(input("Enter the number : "))

for i in range(1,n+1):
  if n%i==0:
    print(i)
