"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    # print(data)
    print_subject_details(data)


def print_subject_details(data):
    """Display subject detail like: subject code, lecturer, number of students """
    for i in data:
        subject = i[0]
        lecturer = i[1]
        number_students = i[2]
        print(f"{subject} is taught by {lecturer} and has {number_students} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    nested_lists = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        nested_lists.append(parts)  # Puts list in a list (LISTCEPTION!)
        # print(nested_lists)
        print("----------")
        # print(nested_lists)
    return nested_lists
    input_file.close()


main()
