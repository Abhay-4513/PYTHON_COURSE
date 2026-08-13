# Accept user input for the upper limit
n = int(input("Enter the value of n: "))

print(f"Even numbers from 1 to {n} are:")
# Start at 2, go up to n (inclusive), and increment by 2
for i in range(2, n + 1,2):
    print(i)
