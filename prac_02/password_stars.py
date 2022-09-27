"""
CP1404/CP5632 - Practical 2
A program that shows password in star format
"""


# imports
# CONSTANTS
MIN_LENGTH = 10


def main():
    """Initiate program"""
    password = input("Password: ")
    password = valid_password(MIN_LENGTH, password)
    count_stars(password)


def count_stars(password):
    """Counts the number of stars"""
    for i in range(len(password)):
        print('*', end='')


def valid_password(min_length, password):
    """Determines validity of password"""
    # used different argument name to avoid errors?
    while len(password) < min_length:
        print("Weak password")
        password = input("Password: ")
    return password


main()
