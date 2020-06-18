# Lists
names = ["Jhon", "Bob", "Mosh", "Sarah", "Alex"]
print(names[0])
print(names[-1])
print(names[2:4])
names[0] = "Jon"
print(names[0])

numbers = [8, 1, 19, 20, 30, 40, 1, 5, 6, 7, 99, 2, 20]
max_value = numbers[0]
for number in numbers:
    if number > max_value:
        max_value = number
print(max_value)
