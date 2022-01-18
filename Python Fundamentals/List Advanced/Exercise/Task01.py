searched_word = input().split(", ")
words = input().split(", ")

answer_list = []

for current_searched_word in searched_word:
    for current_word in words:
        if current_searched_word in current_word:
            if current_searched_word not in answer_list:
                answer_list.append(current_searched_word)

print(answer_list)