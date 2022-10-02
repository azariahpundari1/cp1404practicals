"""
CP1404/CP5632 - Practical 3
To give experience in using different ways to read files
"""

# 1. A code that asks a user for the users input then opens a file called 'name.txt.' and writes their
# name in it

FILE_NAME = 'name.txt'
name = input("Name: ").title()
out_file = open(FILE_NAME, 'w')
print(name, file=out_file)
out_file.close()

