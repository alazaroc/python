# emoji converter
message = input("> ")
# Break message
# Good morning :)
words = message.split(" ")
emojis = {
    ":)": "😀",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
