import re

data = input()
pattern = r"(\@|\#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
matches = re.finditer(pattern, data)
word_pair = len([m.group() for m in re.finditer(pattern, data)])
match_pairs = []

if word_pair:
    print(f"{word_pair} word pairs found!")
else:
    print("No word pairs found!")

for match in matches:
    if match:
        if match.group(2) == match.group(3)[::-1]:
            match_pairs.append(f"{match.group(2)} <=> {match.group(3)}")

if match_pairs:
    print("The mirror words are:")
    print(", ".join(match_pairs))
else:
    print("No mirror words!")



