word = input()

indexes = []

for index, letter in enumerate(word):
    if letter.isupper():
        indexes.append(index)
print(indexes)

