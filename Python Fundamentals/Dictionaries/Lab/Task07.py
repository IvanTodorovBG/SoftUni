n = int(input())
synonyms = {}

for i in range(n):
    word = input()
    synonym = input()

    synonyms.setdefault(word, []).append(synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")


