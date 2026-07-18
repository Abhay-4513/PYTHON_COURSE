# Write a program to accept marks of 6 students and display them in sorted order

marks = []
studnet_1 = int(input(f"Enter the mark of student : "))
marks.append(studnet_1)

studnet_2 = int(input(f"Enter the mark of student : "))
marks.append(studnet_2)

studnet_3 = int(input(f"Enter the mark of student : "))
marks.append(studnet_3)

studnet_4 = int(input(f"Enter the mark of student : "))
marks.append(studnet_4)

studnet_5 = int(input(f"Enter the mark of student : "))
marks.append(studnet_5)

studnet_6 = int(input(f"Enter the mark of student : "))
marks.append(studnet_6)

marks.sort()
print(marks)
