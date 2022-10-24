"""
CP1404 Programming II
A program that asks the user for their email and adds it to a dictionary
Estimate: 6 days
Actual: my soul
"""

email_to_name = {}
email = input("Email: ")
while email != '':
    split_name = email.split('@')
    # print(split_email)  # test
    name = split_name[0]
    email_to_name[email] = name  # key = recipients email
    verify_name = input(f"Is your name {name}? [Y/n] ").upper()
    if verify_name == 'Y' or verify_name == '':
        email_to_name[email] = name
    else:
        new_name = input("Name: ").title()
        email_to_name[email] = new_name
    # print(email_to_name)
    # name = "".join(email_to_name.keys()).title()
    # verify_name = input(f"is your name {name}? [Y/n] ").upper()
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
