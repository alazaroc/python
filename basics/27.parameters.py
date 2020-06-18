# parameters
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("Alex", "xxxx")
greet_user("Mary", "Ross")
# greet_user() # ERROR TypeError: greet_user() missing 1 required positional argument: 'name'
print("Finish")
