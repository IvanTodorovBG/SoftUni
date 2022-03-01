text = input().split(", ")
valid_names = ""

for word in text:
    if 3 <= len(word) <= 16:
        if word.isalnum() or "-" in word or "_" in word:
            valid_names = word
            print(valid_names)
