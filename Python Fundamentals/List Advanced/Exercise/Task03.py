string = input().split(" ")

answer = [current_word for current_word in string if len(current_word) % 2 == 0]

for current_answer in answer:
    print(current_answer)
