# For loops
for price in "Python":
    print(price)

for price in ["Hello", "world", "Extended"]:
    print(price)

for price in [1, 2, 3, 4, 5, 6]:
    print(price)

for price in range(10):
    print(price)

for price in range(5, 10):
    print(price)

for price in range(5, 10, 2):
    print(price)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(total)
print(f"Total: {total}")
