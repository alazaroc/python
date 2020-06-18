# Logical operations
is_high_income = True
is_good_credit = False

if is_high_income and is_good_credit:
    print("OK 1")
else:
    print("NO 1!!")

if is_high_income or is_good_credit:
    print("OK 2")
else:
    print("NO 2!!")

if is_high_income and not is_good_credit:
    print("OK 3")
else:
    print("NO 3!!")
