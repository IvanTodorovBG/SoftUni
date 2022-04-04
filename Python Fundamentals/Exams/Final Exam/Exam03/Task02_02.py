import re

string = input()

pattern = r"([\@|\#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
matches = re.finditer(pattern, string)
is_matches = bool([i.group(0) for i in matches])

word_pairs = []
if is_matches:
    for current in re.finditer(pattern, string):
        word_pairs.append((current.group(2), current.group(3)))
    print(f"{len(word_pairs)} word pairs found!")

    count_mirror_words = sum([1 for kvp in word_pairs if kvp[0] == kvp[1][::-1]])
    if count_mirror_words:
        print("The mirror words are:")
        print(", ".join([f'{kvp[0]} <=> {kvp[1]}' for kvp in word_pairs if kvp[0] == kvp[1][::-1]]))
    else:
        print("No mirror words!")


else:
    print("No word pairs found!")
    print("No mirror words!")