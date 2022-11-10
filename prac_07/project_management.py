"""
CP1404 Programming II - Prac 7
Project
Estimate: 1hr
Actual:
"""


class ProjectManagement:
    """A class representing project management object"""

    def __init__(self, name="", date="", priority=0, cost=0, completion=0):
        """Initiate program taking in project name, date, cost and completion in percenatage"""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return string showing project details"""
        return f"{self.name}, start: {self.date}, priority: {self.priority}, estimate, completion: {self.completion}"

