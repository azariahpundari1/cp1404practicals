CURRENT_YEAR = 2022


class Guitar:
    """A representation of a guitar object"""
    def __init__(self, name="", year=0, cost=0):
        """Initialize a guitars name, year, cost"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string displaying guitar name, year, cost"""
        return f"{self.name} ({self.year}) : {self.cost}"

    def __lt__(self, other):
        """Returns guitar sort from old to new (year)"""
        return other.year > self.year

    def get_age(self):
        """Subtract current year from guitar age, return current age"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if guitar is vintage using guitar age and vintage age (50)"""
        return self.get_age() >= 50
