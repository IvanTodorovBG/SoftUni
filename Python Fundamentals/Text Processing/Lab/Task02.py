text = input().split()
word = ""
for char in text:

    length = len(char)
    word += char * length

print(word)