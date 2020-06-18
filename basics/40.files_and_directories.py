from pathlib import Path
# Absolute path (route in hard disk)
# Relative path

# path = Path("ecommerce")
# print(path.exists())

# path = Path("emails")
# if not path.exists():
#     path.mkdir()

path = Path()
for file in path.glob("*"):
    print(file)
