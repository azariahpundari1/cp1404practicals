"""
CP1404/CP5632 - Practical 2
Score menu program
"""


# import
# Constants
MENU = "(D)isplay result\n(S)tars\n(Q)uit"


def main():
    """Initiate program"""
    print(MENU)
    option = input(">>> ").upper()
    while option != 'Q':
        if option == 'D':
            score = get_score()
            print(get_result(score))
        elif option == 'S':
            score = get_score()
            print('*' * score)
        else:
            print("Invalid choice")
        print(MENU)
        option = input(">>> ").upper()
    print("Finished.")


def get_score():
    """Gets and checks user scores"""
    score = int(input("Score: "))
    # Error loop
    while score > 100 or score < 0:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def get_result(score):
    """Determines results"""
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
