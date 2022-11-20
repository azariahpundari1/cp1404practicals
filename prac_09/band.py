"""
CP1404 Programming II Practical 9
Band class
"""
from prac_09.musician import Musician


class Band(Musician):
    """Represent a band object"""

    def __init__(self, name=""):
        """Initialise a band instance"""
        super().__init__(name)

    def __str__(self):
        """Return a string"""
        return f"{super(Band, self).__str__()}"

    def play(self):
        """Return a string showing band playing"""
        pass

    def add(self, musician):
        """Add a musician to band"""
        pass


# if __name__ == '__main__':
#     from