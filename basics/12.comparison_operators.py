# Comparison operators
temperature = 31
if temperature == 30:
    print("Its a hot day")
else:
    print("Its not a hot day")

name = "Alex"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 30:
    print("Name must be less than 30 characters")
else:
    print("Name OK")
