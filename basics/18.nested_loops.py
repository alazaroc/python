# Nested loops
# (x, y)
# (0, 0)
# ...

for x in range(4):
    # inner loop
    for y in range(3):
        print(f"({x},{y})")

numbers = [5, 2, 5, 2, 2]
for item in numbers:
    print("X" * item)
print(" ----- SEPARATION ------")
for count_x in numbers:
    output = ""
    for count_y in range(count_x):
        output += "X"
    print(output)
