"""
CP1404 Programming II
Estimate = 30min
Actual =
"""


class ProgrammingLanguage:

    def __int__(self, name="", typing="", dynamic="", year=0):
        self.name = name
        self.typing = typing
        self.dynamic = dynamic
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"
