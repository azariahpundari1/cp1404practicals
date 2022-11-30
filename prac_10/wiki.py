"""
CP1404 Practical 10 - APIs & Flask
"""
from wikipedia import wikipedia


def main():
    """Main script that asks user for a page title or phrase"""
    user_input = input("Enter phrase or title: ")
    while user_input != '':
        wiki_output = wikipedia.summary(user_input, 3, 350)
        print(wiki_output)
        user_input = input("Enter phrase or title: ")
    print("Finished.")


main()
