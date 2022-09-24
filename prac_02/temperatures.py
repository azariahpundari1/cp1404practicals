"""
CP1404/CP5632 - Practical 2
A program that converts Celsius to Fahrenheit and vise versa.
Pseudocode for temperature conversion

"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            get_fahrenheit(celsius)
            print(get_fahrenheit(celsius))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            get_celsius(fahrenheit)
            print(get_celsius(fahrenheit))
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return f"Result: {celsius:.2f} C"


def get_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"Result: {fahrenheit:.2f} C"


main()