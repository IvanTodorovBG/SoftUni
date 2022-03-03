text = input()
result = ""
for index in range(len(text)):
    if index == 0:
        result += text[index]
    else:
        if text[index] != text[index -1]:
            result += text[index]

print(result)