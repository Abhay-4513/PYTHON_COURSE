#  Write a program to count the number of vowels and consonants in a 

string = input("Enter a word: ")
vowels = 0
consonants = 0
for i in string:
    if i.lower() in 'aeiou':
        vowels += 1
    elif i.isalpha():
        consonants += 1

print(f"The number of vowels in the string is: {vowels}")
print(f"The number of consonants in the string is: {consonants}")