"""
CP1404/CP5632 - Practical 1
Loops
A program consisting of various for loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
# prints numbers from 0 to 100 in increments of 10
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b
# prints numbers from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
# Prints the amount of stars specified
number_of_stars = int(input("Number of stars: "))
for i in range(0, number_of_stars):
    print('*', end='')

# d
# Prints the stars per line
# could this have been done better?
for i in range(0, number_of_stars+1):
    print(i * '*', sep='')
