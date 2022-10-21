"""
CP1404 Programming II
A program that displays colours and their hex decimal
"""

COLOUR_TO_HEX = {"Absolute Zero": "#0048ba", "AliceBLue": "#f0f8ff", "Acid Green": "#b0bf1a", "Amaranth": "#e52b50",
                 "Amethyst": "#9966cc", "Amber": "#ffnbf00", "Aqua": "#00ffff", "Apricot": "#fbceb1",
                 "Beaver": "#9f8170", "Banana Yellow": "#ffe135"}

run = True
while run:
    try:
        colour_name = input("Enter colour name: ").title()
        while colour_name != "":
            print(COLOUR_TO_HEX[colour_name])
            colour_name = input("Enter colour name: ").title()
        run = False
    except KeyError:
        print("Invalid colour name")
