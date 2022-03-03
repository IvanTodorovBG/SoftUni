text = input()

for index, letter in enumerate(text):
    if letter == ":":
        print(letter + text[index + 1])

