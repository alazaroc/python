# dis
# dictionaries: store key value pairs
# Name: Alex xxx
# Email: xxxx@xxxx.com
# Phone: 1234

# customer = {
#     "name": "Alex xxxx",
#     "age": 30,
#     "age": 40, # override previous
#     "is_verified": True
# }
# print(customer)
# print(customer["name"])
# # print(customer["birthday"]) # error, key doesn't exist
# print(customer.get("birthday")) # return NONE - no value
# print(customer.get("name"))
#
# customer["name"] = "Jack Smith"
# print(customer.get("name"))
#
# customer["birthday"] = "23 03 1986"
# print(customer.get("birthday"))

# Exercise
phone = input("Phone: ")
# print(phone)
# for number in phone:
#     if number is 1:
#         print("One")
#     elif number is 2:
#         print("Two")
#     elif number is 3:
#         print("Three")
#     elif number is 4:
#         print("Four")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
