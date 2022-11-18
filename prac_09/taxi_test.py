"""
CP1404 Programming II Practical 9
Taxi tests
"""

from prac_09.taxi import Taxi


def main():
    """Test to see if taxi.py works"""
    my_taxi = Taxi("Prius", 100, 1.23)
    # print(my_taxi)
    # drive taxi 40km
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    print(my_taxi)


main()
