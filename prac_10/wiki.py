"""
CP1404 Practical 10 - APIs & Flask
"""
from wikipedia import wikipedia
from wikipedia import exceptions


def main():
    """Main script that asks user for a page title or phrase"""
    user_input = input("Enter phrase or title: ")
    while user_input != '':
        # pycharm suggested to add this to avoid BeautifulSoup package
        wiki_title = wikipedia.search(user_input, 1)
        wiki_title_str = " ".join(wiki_title)
        wiki_summary = wikipedia.summary(user_input)
        print(f"{wiki_title_str}\n{wiki_summary}")


# okay, idk why its not working and ive tried using the exception handling but it keeps saying its running two
# exceptions

main()
