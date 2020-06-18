# inheritance
# BAD PRACTICE
# class Dog:
#     def walk(self):
#         print("walk")
#
#
# class Cat:
#     def walk(self):
#         print("walk")


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    # Indicate PASS to do nothing (its OK, is empty)
    # pass
    def bark(self):
        print("bark")


class Cat(Mammal):
    # pass
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()
