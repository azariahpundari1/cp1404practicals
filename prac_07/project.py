"""
CP1404 Programming II - Prac 7
Project
Estimate: 1hr, start - 7:36pm thursday 10th nov
Actual: ...
"""

# Constants
MENU = '(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects (date)\n(A)dd project\n(U)pdate ' \
       'project\n(Q)uit'

FILE_NAME = 'projects.txt'

def main():
    print(MENU)
    option = input(">>> ").upper()
    while option != 'Q':
        if option == 'L':
            in_file = open(FILE_NAME, 'r')
        elif option == 'S':
            pass
        elif option == 'D':
            pass
        elif option == 'F':
            pass
        elif option == 'A':
            pass
        elif option == 'U':
            pass
        else:
            print("Invalid input")
        print(MENU)
        option = input(">>> ").upper()


main()
