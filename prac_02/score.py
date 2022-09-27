"""
CP1404/CP5632 - Practical 2
A program that determines the result from a given score
"""
import random


def main():
    """Initiate program"""
    score = float(input("Enter score: "))
    print(get_result(score))
    random_number = random.randint(0, 100)
    # print(f"Random score: {random_number}")
    get_result(random_number)
    print(get_result(random_number))


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
