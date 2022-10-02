"""
CP1404/CP5632 - Practical 3
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # checks if the denominator is 0, if 0 it asks for the denominator again
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. When will ValueError occur?
# When the user inputs an invalid value - a string instead of an int

# 2. When will a ZeroDivisionError occur?
# When the user inputs a 0 in the denominator

# 3. Could you change the code to avoid the possibility of a zero division?
# Yes, use a while loop to check for invalid numbers.
