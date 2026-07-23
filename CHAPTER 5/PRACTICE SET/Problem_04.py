# Create an empty dictionary. Allow 4 friends to enter their favourite languages as value and use keys as their names. Assume that their name is unique

lang = {}

fr1 = input("Enter your name : ")
lang1 = input("Enter your favourite language : ")
lang.update({fr1:lang1})

fr2 = input("Enter your name : ")
lang2 = input("Enter your favourite language : ")
lang.update({fr2:lang2})

fr3 = input("Enter your name : ")
lang3 = input("Enter your favourite language : ")
lang.update({fr3:lang3})

fr4 = input("Enter your name : ")
lang4 = input("Enter your favourite language : ")
lang.update({fr4:lang4})

print(lang)