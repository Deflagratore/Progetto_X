from random import randint

class Dado:
    """Una classe che rappresenta un dado"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
        