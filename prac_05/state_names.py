"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
run = True

while run:
    try:
        state_code = input("Enter short state: ").upper()
        print(state_code, "is", CODE_TO_NAME[state_code])
        run = False
    except KeyError:
        print("Invalid short state")

# displays every state code and state name
for state_code in CODE_TO_NAME.items():
    print(f"{state_code[0]} is {state_code[1]}")
