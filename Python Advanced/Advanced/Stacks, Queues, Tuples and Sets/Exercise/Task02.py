from collections import deque

expression = deque(input().split())
numbers = []

while expression:

    current_char = expression.popleft()
    if current_char.isdigit():
        numbers.append(int(current_char))
    elif current_char.lstrip("-").isdigit():
        numbers.append(int(current_char))
    else:

        if current_char == "-":
            current_result = numbers[0]
            for num in numbers[1:]:
                current_result -= num
            numbers.clear()
            numbers.append(current_result)

        elif current_char == "+":
            current_result = sum(numbers)
            numbers.clear()
            numbers.append(current_result)

        elif current_char == "/":
            current_result = numbers[0]
            for num in numbers[1:]:
                current_result /= num
            numbers.clear()
            numbers.append(int(current_result))

        elif current_char == "*":
            current_result = 1
            for num in numbers:
                current_result *= num
            numbers.clear()
            numbers.append(current_result)

print(''.join([str(num) for num in numbers]))
