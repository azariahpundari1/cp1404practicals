"""
CP1404 Programming II - Prac 7
Project
Estimate: 1hr, start - 7:36pm thursday 10th nov
Actual: ...
"""


# Imports
from prac_07.project_management import ProjectManagement
import datetime
# Constants
MENU = '(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects (date)\n(A)dd project\n(U)pdate ' \
       'project\n(Q)uit'

FILE_NAME = 'projects.txt'


def main():
    print(MENU)
    projects = []
    option = input(">>> ").upper()
    while option != 'Q':
        if option == 'L':
            load_project(projects)
        elif option == 'S':
            pass
        elif option == 'D':
            incomplete_projects = []
            complete_projects = []
            for project in projects:
                completion = float(project[4])
                if completion != 100:
                    incomplete_projects.append(project)
                else:
                    complete_projects.append(project)
            print("Incomplete projects:")

            for project in incomplete_projects:
                print(ProjectManagement(project[0], project[1], project[2], project[3], project[4]))
            print("Completed projects:")
            for project in complete_projects:
                print(ProjectManagement(project[0], project[1], project[2], project[3], project[4]))
        elif option == 'F':
            date_string = input("Date (dd/mm/yyyy): ")  # e.g., "30/9/2022"
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            # skipping this one cause i dont get it
            # print(f"That day is/was {date.strftime('%A')}")
            # print(date.strftime("%d/%m/%Y"))
        elif option == 'A':
            new_project = []
            print("Lets add a new project")
            name_of_project = input("Project name: ")
            new_project.append(name_of_project)
            date_started = input("Date (dd/mm/yyyy): ")
            new_project.append(date_started)
            priority = int(input("Priority: "))
            new_project.append(priority)
            estimate_cost = float(input("Estimate cost: "))
            new_project.append(estimate_cost)
            completion = float(input("Percent complete: "))
            new_project.append(completion)
            projects.append(new_project)
        elif option == 'U':
            for i, project in enumerate(projects):
                print(f"{i+1} {ProjectManagement(project[0], project[1], project[2], project[3], project[4])}")
            choice = int(input("Project choice: "))
            project_choice = ProjectManagement(choice)  # idk what to do here :/
            print(project_choice)
        else:
            print("Invalid input")
        print(MENU)
        option = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def load_project(projects):
    """Load project from user input"""
    # file_name = input("File name followed by .txt, .csv etc: ")
    in_file = open(FILE_NAME, 'r')  # to make tests run quicker
    in_file.readline()
    for line in in_file:
        # print(line)
        parts = line.strip().split('\t')
        projects.append(parts)
    in_file.close()


main()
