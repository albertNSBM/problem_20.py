from collections import defaultdict, Counter
str1 = input("enter string:")
dictionary = {}
for letter in str1:
    dictionary[letter] = dictionary.get(letter, 0) + 1  # function to get every letter
print(dictionary)