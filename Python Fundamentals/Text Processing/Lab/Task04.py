banned_words = input().split(", ")
text = input()

for word in banned_words:

    while word in text:
        length = len(word)
        text = text.replace(word, ("*" * length))

print(text)
