# Write a program to accept marks of 6 students and display them in sorted order

marks = []

for i in range(1,7):
    studnet = int(input(f"Enter the mark of student {i} : "))
    marks.append(studnet)
    marks.sort()
print(marks)
