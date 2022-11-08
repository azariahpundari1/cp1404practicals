from prac_06.guitar import Guitar


def main():
    """Start of program"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    print(f"My guitar: {name}, first made in {year}")

    guitar = Guitar(name, year, cost)
    print(guitar)

    print(f"{guitar.name} get_age() - Expected {50}. Got {guitar.get_age()}")
    print()
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")


main()
