# If statement
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Enjoy your day")
elif is_cold:
    print("Is cold")
else:
    print("NO HOT")
print("always executed")

house_price = 1000000
has_buyer_good_credit = True

if has_buyer_good_credit:
    house_price -= 100 * 10
else:
    house_price -= 100 * 20
print(house_price)
