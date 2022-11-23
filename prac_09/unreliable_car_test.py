"""
CP1404 Programming II practical 9
Test unreliable_car
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test to see if unreliable_car.py works"""
    reliable_car = UnreliableCar("Reliable Car", 100, 100)
    unreliable_car = UnreliableCar("Unreliable Car", 100, 10)
    print(reliable_car)
    print(unreliable_car)
    reliable_car.drive(20)
    unreliable_car.drive(20)
    print(reliable_car)
    print(unreliable_car)
    reliable_car.drive(20)
    unreliable_car.drive(20)
    print(reliable_car)
    print(unreliable_car)
    reliable_car.drive(10)
    unreliable_car.drive(10)
    print(reliable_car)
    print(unreliable_car)


main()
