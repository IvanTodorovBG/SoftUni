text = input()
result = ""
strength = 0

for index in range(len(text)):
    char_in_text = text[index]

    if char_in_text == ">":
        strength += int(text[index + 1])
        result += char_in_text
    elif strength != 0:
        strength -= 1
    else:
        result += char_in_text

print(result)