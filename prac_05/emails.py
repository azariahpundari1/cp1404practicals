"""
CP1404 Programming II
A program that asks the user for their email and adds it to a dictionary
Estimate: 6 days
Actual: my soul
"""

email_to_name = {}


def main():
    """Initiate program"""
    email = input("Email: ")
    while email != '':
        split_email = email.split('@')
        # print(split_email)  # test
        full_name = split_email[0]
        split_name = full_name.split('.')
        name = " ".join(split_name).title()
        # print(name)  # test
        set_name(email, name)
        verify_name = input(f"Is your name {name}? [Y/n] ").upper()
        if verify_name == 'Y' or verify_name == '':
            # keeps value as current name
            set_name(email, name)
        else:
            # sets value as new name
            new_name = input("Name: ").title()
            set_name(email, new_name)
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name.title()} ({email})")


def set_name(email, name):
    """Function that sets the name for the dictionary"""
    email_to_name[email] = name  # key = recipients email


main()