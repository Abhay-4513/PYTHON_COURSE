#This program will the output of this series : 1^2 + 2^2 + 3^2 + ... + n^2.
n = int(input("Enter the number : "))
a = 0
c = []
for i in range(1,n+1):
  b = i*i
  a = a + b
  c.append(b)
print("The series is : ", c)
print("The sum of the series is : ", a)
