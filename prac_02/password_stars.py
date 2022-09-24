"""Module docstring"""


# imports
# CONSTANTS

def main():
    """Function docstring"""
    password = input("Password: ")
    MIN_LENGTH = 10
    password = get_password(MIN_LENGTH, password)
    get_stars(password)


def get_stars(password):
    for i in password:
        print('*', end='')


def get_password(MIN_LENGTH, password):
    while len(password) < MIN_LENGTH:
        print("Weak password")
        password = input("Password: ")
    return password


main()
