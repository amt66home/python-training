import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        # to return a tuple you can leave out the brackets and Python will automatically interpret it as a tuple
        return first, second

dice = Dice()
print(dice.roll())