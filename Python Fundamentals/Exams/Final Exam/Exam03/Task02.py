import re

data = input()
pattern = r"(\@|\#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"

matches = re.finditer(pattern, data)
match_list_first_words = []
match_list_first_words_reverse = []
match_list_second_words = []
word_found = False

for match in matches:
    match_list_first_words.append(match.group(2))
    match_list_second_words.append(match.group(3))

for i in range(len(match_list_first_words)):
    match_list_first_words_reverse.append(match_list_first_words[i][::-1])

if match_list_first_words:
    print(f"{len(match_list_first_words)} word pairs found!")
else:
    print("No word pairs found!")

for word in match_list_first_words_reverse:
    if word in match_list_second_words:
        word_found = True

if word_found:
    print("The mirror words are:")
else:
    print("No mirror words!")

answer = []

for word in match_list_first_words_reverse:
    if word in match_list_second_words:
        answer.append(f"{word[::-1]} <=> {word}")
print(", ".join(answer))



