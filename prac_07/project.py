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
            projects = []
            load_project(projects)
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
    print("Thank you for using custom-built project management software.")


def load_project(projects):
    """Load project from user input"""
    # file_name = input("File name followed by .txt, .csv etc: ")
    in_file = open() # to make tests run quicker
    in_file.readline()
    for line in in_file:
        # print(line)
        parts = line.strip().split('  ')
        projects.append(parts)
    print(projects)
    in_file.close()


main()
