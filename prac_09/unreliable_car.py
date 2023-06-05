"""
CP1404 Programming II practical 9
Unreliable car class that inherits from Car
"""

from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of Car that includes reliability"""

    def __init__(self, name, fuel, reliability=0):
        """Initialise a unreliable car instance"""
        super().__init__(name, fuel)
        self.reliability = reliability
        self.distance = 0

    def __str__(self):
        """Return a string representation of an UnreliableCar object."""
        return f"{self.name}, fuel={self.fuel}, distance travelled={self.distance}km"

    def drive(self, distance):
        """Drive car a certain distance"""
        if self.reliability > random.randint(0, 100):
            distance_driven = super().drive(distance)
            self.distance += distance_driven
        return distance
