"""Band class for CP1404"""
from musician import Musician


class Band:
    """Band class"""

    def __init__(self, band_name=""):
        """Construct a Band with a band name and an empty musicians collection"""
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        print("Band string")
        return f"{self.band_name} ({self.musicians[4]})"

    def __repr__(self):
        print("Repr string")
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        pass
