"""
CP1404 Practical
A program that asks the user how many quick picks they wish to generate then generates
that many lines of output
"""

# Imports
import random

# Constants
MAX_LINE = 6
MAX_NUMBER = 45
MIN_NUMBER = 1
# print(LINE_NUMBER)
# print(len(LINE_NUMBER))


def main():
    quick_pick = int(input("How many quick picks? "))

    for row in range(quick_pick):
        new_list = []
        for columns in range(MAX_LINE):
            random_number = random.randint(1, 45)
            if random_number not in new_list:
                new_list.append(random_number)
        print(new_list, end='')
        # print(''.join(str(new_list)), end='')
        print()

# i wanna keep working on this, i just have a driving test tomorrow and i need to sleep, this was fun tho


main()
