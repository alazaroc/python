# List methods
numbers = [5, 3, 1, 7, 4]
# numbers.append(13)
# print(numbers)
# numbers.insert(0, 10)
# print(numbers)
# numbers.remove(5)
# print(numbers)
# numbers.pop()
# print(numbers)
#
# print(numbers.index(1))
# print(numbers.index(99))
#
# numbers.clear()
# print(numbers)
# print(60 in numbers)
# print(numbers.count(5))
# numbers = [5, 3, 1, 5, 7, 4]
# print(numbers.count(5))
# print(numbers.sort())
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)

# Exercise: delete duplicate in a list
numbers = [1, 1, 14, 4, 5, 3, 1, 5, 7, 4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
