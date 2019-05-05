import random

class Dice:

    def __init__(self, type):
        self._types = [3, 4, 6, 8, 10, 12, 20, 100]
        self.type = type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type in self._types:
            self._type = type
        else:
            self._type = 6

    def roll(self):
        return random.randint(1, self.type)

d = Dice(10)

print(d.roll())