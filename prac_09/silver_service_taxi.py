"""
CP1404 Programming II Practical 9
Silver Service Taxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent silver service taxi object derived from taxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialize a silver service taxi instance"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        """Return a string displaying name, fuel, odo, distance, price per km, flagfall"""
        return f"{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance}km on current fair, " \
               f"${self.price_per_km}/km plus flagfall of {self.flagfall}"

    def get_fare(self):
        """Return price for silver service trip"""
        return self.flagfall * self.fanciness


if __name__ == '__main__':
    # tests
    test = SilverServiceTaxi("Hammer", 200, 4)
    print(test)
    test.drive(20)
    print(test)
    test.start_fare()
    print(test)
