"""
CP1404 Programming II Practical 9
Band class
"""


class Band:
    """Represent a music band instance"""

    def __init__(self, name):
        """Initialise band instance"""
        self.name = name
        self.musicians = []
        
    def __str__(self):
        """Return a string representation of a band, showing the variables"""
        return f"{self.name} ({self.musicians}"

    def add(self, musician):
        """Add a musician to musician's collection."""
        # self.musicians.append(musician)

    def play(self):
        """Return a string displaying band, band members with their instruments."""
        if not self.instruments:
            return f"{self.name} needs an instrument!"
        return f"{self.name} is playing: {self.instruments[0]}"


if __name__ == '__main__':
    from musician import Musician
    from guitar import Guitar


    def main():
        band = Band("Extreme")
        nuno = Musician("Nuno Bettencourt")
        nuno.add(Guitar("Washburn N4", 1990, 2499.95))
        nuno.add(Guitar("Takamine acoustic", 1986, 1200.0))
        band.add(nuno)
        band.add(Musician("Gary Cherone"))
        pat = Musician("Pat Badger")
        pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.0))
        band.add(pat)
        kevin = Musician("Kevin Figueiredo")
        band.add(kevin)

        print("band (str)")
        print(band)
        print("band.play()")
        print(band.play())


    main()
