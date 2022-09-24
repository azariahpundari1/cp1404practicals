password = input("Password: ")
MIN_LENGTH = 10
while len(password) < MIN_LENGTH:
    print("Weak password")
    password = input("Password: ")
for letter in password:
    print('*', end='')
