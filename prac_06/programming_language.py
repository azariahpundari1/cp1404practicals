"""
CP1404 Programming II
Estimate = 30min
Actual =
"""


class ProgrammingLanguage:

    def __init__(self, name, typing, dynamic, year):
        """My one"""
        self.name = name
        self.typing = typing
        self.dynamic = dynamic
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.dynamic}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
