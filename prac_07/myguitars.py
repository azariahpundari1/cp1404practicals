"""
CP1404 Programming II - Prac 07
My guitars
"""

from prac_06.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """A program that displays a collection of guitars using a class"""
    guitars = load_file()
    guitars.sort()
    # display guitar
    for guitar in guitars:
        print(guitar)


def load_file():
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        # print(line)  # test
        parts = line.strip().split(',')
        # print(parts)  # test
        name = parts[0]
        year = parts[1]
        price = parts[2]
        guitar = Guitar(name, year, price)
        guitars.sort()
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
