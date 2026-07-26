# Write a program to find out whether a student passed or failed if it requires a total 40% and atleast 33% in each subjects to pass. Assume 3 subjects and take marks as an input from the user.

sub_1 = int(input("Enter the Maths marks : "))
sub_2 = int(input("Enter the Physics marks : "))
sub_3 = int(input("Enter the Python marks : "))

print(f"Maths score : {sub_1/100}")
print(f"Physics score : {sub_2/100}")
print(f"Python score : {sub_3/100}")

percentage = ((sub_1+sub_2+sub_3)/300)*100
print(percentage)

if ((sub_1/100)>=0.33 and (sub_2/100)>=0.33 and (sub_3/100)>=0.33 and percentage>=40):
    print("you are passed...")

else:
    print("you are failed")
    print("Because either your percentage is less than 40 or any one subject has less than 0.33")