text = input().split()
new_list = []
result = 0
divide = 0
multiply = 0
subtract = 0
add = 0

for current_word in text:
    first_char = current_word[0]
    last_char = current_word[-1]
    number = int(current_word[1:-1])

    if first_char.isupper():
        divide = number / (ord(first_char) - 64)
        result += divide
    else:
        multiply = number * (ord(first_char) - 96)
        result += multiply

    if last_char.isupper():
        subtract = result - (ord(last_char) - 64)
        result = subtract
    else:
        add = result + (ord(last_char) - 96)
        result = add
x = round(result, 2)
print(f"{x:.2f}")

