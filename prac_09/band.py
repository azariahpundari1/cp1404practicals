"""Band class for CP1404"""


class Band:
    """Band class"""

    def __init__(self, band_name: str):
        """Construct a Band with a name and empty musician collection"""
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a musician"""
        return f"{self.band_name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of a musician showing variables"""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to musicians collection"""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their song or no instrument"""
        pass


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
