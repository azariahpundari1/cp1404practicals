"""
CP 1404 Programming II
A program that counts the number of occurrences of words
Estimate: 50 minutes
Acutal: 3 days
"""


word_dict = {}

string = input("Text: ")
words = string.split()
# print(words)
for word in words:
    # print(word)
    # counting the words, thank you lindsay for the lecture notes, true life-saver
    word_dict[word] = word_dict.get(word, 0) + 1

# display the words and count
for word, frequency in sorted(word_dict.items()):  # displays sorted dictionary
    print(f"{word:<10} : {frequency}")
