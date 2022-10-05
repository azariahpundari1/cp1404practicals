"""
CP1404/CP5632 Practical
An exercise to do with lists, to be precise: numbers
"""

numbers = []

for i in range(1, 5+1):
    # print(i)
    try:
        number = int(input("Number: "))
        numbers.append(number)
    except ValueError:
        print("Not a number")
    # hmm, interesting how it keeps going for the set amount of times
    # how is a try different from a while error check? can i make it ask for a number but not iterate through the
    # for loop?



# First number
print(f"The first number is {numbers[0]}")

# Last number
print(f"The last number is {numbers[-1]}")

# Smallest number
print(f"The smallest number is {min(numbers)}")

# Largest number
average = sum(numbers) / len(numbers)
print(f"The average of the number is {average}")