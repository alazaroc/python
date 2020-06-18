# keyboard parameters: increase readability of the code
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user(last_name="xxx", first_name="Alex")
# Example of use
# calc_cost(total=50, shipping=5, discount=0,1)
# keyboard_argument AFTER positional argument is OK, not reverse
# greet_user(last_name="xxx", "Alex")
# greet_user("xxx", first_name="Alex")
print("Finish")
