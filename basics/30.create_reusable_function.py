# reusable function
def emoji_converter(message):
    global output
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "


input_text = input("> ")
emoji_converter(input_text)
print(output)
