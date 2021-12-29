numbers = input().split(" ")
string = list(input())

answer = []
indexes = []

for current_number in numbers:
    sum_of_digits = 0
    for current_digit in current_number:
        current_digit = int(current_digit)
        sum_of_digits += current_digit
    indexes.append(sum_of_digits)

for current_index in indexes:
    if 0 <= current_index < len(string):
        answer.append(string[current_index])
        string.pop(current_index)
    else:
        current_index = current_index % len(string)
        answer.append(string[current_index])
        string.pop(current_index)

print("".join(answer))