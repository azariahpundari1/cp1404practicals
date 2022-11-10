"""
CP1404 Programming II - Prac 07
My guitars
"""

from prac_06.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """A program that displays a collection of guitars using a class"""
    guitars = load_file()
    # display guitar
    guitars.sort()
    # print(type(guitars[0][1]))  # test
    for guitar in guitars:
        guitar_object = Guitar(guitar[0], guitar[1], guitar[2])
        print(guitar_object)
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
            print(new_guitars)
            guitars.append(new_guitars)
        else:
            run = False
    save_file(FILENAME, guitars)


def save_file(FILENAME, guitars):
    """Save file containing any new guitar inputted by user"""
    out_file = open(FILENAME, 'w')
    for i, guitar in enumerate(guitars):
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
        guitars.append(parts)
    in_file.close()
    return guitars


main()
