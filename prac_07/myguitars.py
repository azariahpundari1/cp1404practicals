"""
CP1404/CP5632 Practical 07 - My Guitars
Guitars
"""

from prac_06.guitar import Guitar

file_name = 'guitars.csv'


def main():
    """Read guitars from guitars.csv, store in list, display"""
    guitars = []
    in_file = open(file_name, 'r')
    in_file.readline()  # skips first line format/protocol
    for line in in_file:
        parts = line.strip().split(',')
        # print(parts)
        # print(parts[0])  # test
        name = parts[0]
        year = parts[1]
        price = parts[2]
        guitar = Guitar(name, year, price)
        guitars.append(guitar)
    in_file.close()

    # Sort guitars from oldest - newest
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
