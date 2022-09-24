"""
CP1404/CP5632 - Practical 1
A program that converts Celsius to Fahrenheit and vise versa.
Pseudocode for temperature conversion
display menu
get choice
while choice != Q
    if choice  = C
        get celsius
        fahrenheit = celsius * 9.0 / 5 = 32
        display result
    else if choice = F
        get fahrenheit
        celsius = 5 / 9 * (fahrenheit - 32)
        display result
    else
        display invalid option
    display menu
    get choice
display thank you
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
