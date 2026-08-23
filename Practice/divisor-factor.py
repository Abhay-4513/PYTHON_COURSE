# This program will give the factors which are perfect divisors of the given number.
n = int(input("Enter the number : "))
a = []
for i in range(1,n+1):
  if n%i==0:
    a.append(i)

print(a)
print(f"Number of divisors: {len(a)}")
