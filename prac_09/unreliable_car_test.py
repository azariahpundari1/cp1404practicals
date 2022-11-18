"""
CP1404 Programming II practical 9
Test unreliable_car
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test to see if unreliable_car.py works"""
    car = UnreliableCar("Car", 100, 100)
    print(car)
    car.drive(20)
    print(car)
    car.drive(20)
    print(car)
    car.drive(10)
    print(car)


main()
