# Search in google: python 3 module index
# https://docs.python.org/3/py-modindex.html

import random
# for i in range(3):
#     # random between 0 and 1
#     # print(random.random())
#     # random between 10 and 20
#     print(random.randint(10,20))

# members = ["Alex", "Sophie", "Martha", "Jhon"]
# leader = random.choice(members)
# print(leader)

# Exercise: roll a dice with different values (1,1), (5, 6)
# Dice
# - roll() - tuple with 2 values


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
