"""
CP1404/CP5632 - Practical 1
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")

# could we also use
# 'elif score < 50:
#       print("Bad")
# or is this bad practice?
