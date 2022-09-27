"""
CP1404/CP5632 - Practical 2
A program that shows password in star format
"""


# imports
# CONSTANTS

def main():
    """Initiate program"""
    password = input("Password: ")
    MIN_LENGTH = 10
    password = valid_password(MIN_LENGTH, password)
    count_stars(password)


def count_stars(password):
    """Counts the number of stars"""
    for i in range(len(password)):
        print('*', end='')


def valid_password(MIN_LENGTH, password):
    """Determines validity of password"""
    while len(password) < MIN_LENGTH:
        print("Weak password")
        password = input("Password: ")
    return password


main()
