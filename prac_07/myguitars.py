"""
CP1404/CP5632 Practical 07 - My Guitars
Guitars
"""

from prac_06.guitar import Guitar

file_name = 'guitars.csv'
MENU = '(A)dd guitar\n(D)isplay guitar\n(Q)uit'


def main():
    """Read guitars from guitars.csv, store in list, display"""
    guitars = []
    new_guitar = []
    load_file(guitars)
    # Sort guitars from oldest - newest
    guitars.sort()
    display_guitars(guitars)
    print(f"You have {len(guitars)} guitars in your collection")

    # going to make this similar to assessment01 because without a menu, its confusing
    print(MENU)
    option = input(">>> ").upper()
    while option != 'Q':
        if option == 'D':
            display_guitars(guitars)
        elif option == 'A':
            name = input("Name: ").title()
            year = int(input("Year: "))
            price = float(input("Price: "))
            guitar_to_append = append_guitar(name, new_guitar, price, year)
            guitars.append(guitar_to_append)
        else:
            print("Invalid input")
            print(MENU)
        option = input(">>> ").upper()
    print("Fin")
    save_file(file_name, guitars)


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def load_file(guitars):
    in_file = open(file_name, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        # print(parts)
        # print(parts[0])  # test
        guitar = identify_guitar_parts(parts)
        guitars.append(guitar)
    in_file.close()


def append_guitar(name, new_guitar, price, year):
    """Append new guitar into list - new_guitar"""
    new_guitar.append(name)
    new_guitar.append(year)
    new_guitar.append(price)
    return identify_guitar_parts(new_guitar)


def identify_guitar_parts(parts):
    """Identify guitar parts into variables, creates guitar object using class"""
    name = parts[0]
    year = parts[1]
    price = parts[2]
    guitar = Guitar(name, str(year), str(price))
    return guitar


def save_file(file_name, guitars):
    out_file = open(file_name, 'w')
    for i, guitar in enumerate(guitars):
        str_guitar = [str(guitar) for guitar in guitar]
        print(",".join(str_guitar), file=out_file)
    out_file.close()


main()
