# Weight converter
weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

unit_long = ""
weight_calculated = 0
if unit.lower() == "k":
    unit_long = "pounds"
    weight_calculated = float(weight) / 0.45
elif unit.lower() == "l":
    unit_long = "kg"
    weight_calculated = float(weight) * 0.45
else:
    print("ERROR, wrong data")
print(f"You are {weight_calculated} {unit_long}")
