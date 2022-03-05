text = input()
used_text = ""
result = ""
convert = ""
symbols = ""
index = 0

while index < len(text):
    convert = ""
    letter = text[index]

    if letter.isdigit():
        if (index + 1) < len(text) and text[index + 1].isdigit():
            convert = text[len(used_text):index]
            used_text += convert + letter + text[index + 1]
            number = int(text[index] + text[index + 1])
            result += convert.upper() * number
            index += 2
        else:
            convert = text[len(used_text):index]
            used_text += convert + letter
            result += convert.upper() * int(letter)
            index += 1
    else:
        index += 1

for char in result:
    if char not in symbols:
        symbols += char

print(f"Unique symbols used: {len(symbols)}")
print(result)
