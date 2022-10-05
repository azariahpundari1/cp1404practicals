"""
CP1404/CP5632 Practical
A testing area for subject_reader.py
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    things = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        things.append(parts)
    print(things)
    input_file.close()


main()
