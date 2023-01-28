class Point:
    # CONSTRUCTOR
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
# point.x = 10
print(point.x)


# Exercise:
# Person
#  - name
#  - talk()
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person = Person("Alejandro")
person.talk()

bob = Person("Bob")
bob.talk()
