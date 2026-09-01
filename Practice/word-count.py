# Write a program to count the number of words in a sentence 

word = input("Enter a sentence : ")

words = word.split()
word_count = len(words)
print(f"The number of words in the sentence is: {word_count}")