"""
CP1404 Programming II - Prac 07
My guitars
Estimate: 30 min
Actual: literally 2 days, i lost count glad i got it done tho and it works
"""

from prac_06.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """A program that displays a collection of guitars using a class"""
    guitars = load_file()
    guitars_csv = load_csv_data()
    # display guitar
    # print(type(guitars[0][1]))  # test
    display_guitars(guitars)
    run = True
    while run:
        new_guitars = []
        name = input("Name: ")
        if name != "":
            new_guitars.append(name)
            year = int(input("Year: "))
            new_guitars.append(year)
            price = float(input("Price: "))
            new_guitars.append(price)
            guitars.append(Guitar(new_guitars[0], new_guitars[1], new_guitars[2]))
            guitars_csv.append(new_guitars)
        else:
            run = False
    display_guitars(guitars)  # to show new guitars if user has inputted new guitars
    save_file(guitars_csv)


def display_guitars(guitars):
    """Display guitar, sort from oldest to newest"""
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def save_file(csv_data):
    """Save file containing any new guitar inputted by user"""
    out_file = open(FILENAME, 'w')
    for i, guitar in enumerate(csv_data):
        str_guitar = [str(guitar) for guitar in guitar]
        print(",".join(str_guitar), file=out_file)
    out_file.close()


def load_file():
    """Loads guitars from file, sorts data, stores guitars in list"""
    guitars = []
    in_file = open(FILENAME, 'r')
    for line in in_file:
        # print(line)  # test
        parts = line.strip().split(',')
        # print(parts)  # test
        parts[1] = int(parts[1])
        parts[2] = float(parts[2])
        guitars.append(Guitar(parts[0], parts[1], parts[2]))  # this took me so long to figure out
    in_file.close()
    return guitars


def load_csv_data():
    guitars_csv = []  # to save onto csv file
    in_file = open(FILENAME, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        parts[1] = int(parts[1])
        parts[2] = float(parts[2])
        guitars_csv.append(parts)
    in_file.close()
    return guitars_csv


main()
