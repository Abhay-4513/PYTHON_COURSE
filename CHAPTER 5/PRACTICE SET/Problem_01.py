# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

meaning = {
    "Haath":"Hand",
    "Aankh":"Eye",
    "Ghar":"House",
    "Neela":"Blue",
    "Hara":"Green",
    "Kshma":"Sorry"
}

print(meaning.keys())
print("Above are the Hindi words , choose the word you wan't to know the meaning in English..")

user = input("Enter the word : ")

print(f"{meaning[user]}")
# print(f"The meaning of {user} is : {meaning.pop(user)}") # This is the another way...
