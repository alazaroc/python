# modules - organize CODE (2 approaches)
import utils
import converters
from converters import kg_to_lbs  # all functions
print(kg_to_lbs(100))
print(converters.kg_to_lbs(70))


# Exercise
numbers = [8, 1, 19, 20, 30, 40, 1, 5, 6, 7, 99, 2, 20]
print(utils.find_max(numbers))
print(utils.find_max2(numbers))
print(max(numbers))
