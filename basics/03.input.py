# Input from the user
name = input('What is your name? ')
color = input('What is your favourite color? ')
print("Hi ", name, 'likes ', color)
birth_year = input('Birth: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)
weight_lbs = input("What is your weigh in pounds?")
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)