"""
CP1404/CP5632 - Practical 1
Shop Calculator
A program that asks the user for the number of products and the price
in order to calculate total cost for all items.
Pseudocode:
DISCOUNT = 100
total_price = 0
get number_of_items
for item in number_of_items
    get item_price
    total_price = total_price + item_price
if total_price > 100
    total_price * 0.1
    display total_price
else:
    display total_price
"""

DISCOUNT = 0.1
total_price = 0
number_of_items = int(input("Number of price: "))
# error loop
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for item in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
# this calculates discount price
if total_price > 100:
    discount_price = total_price * DISCOUNT
    total_price -= discount_price
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
