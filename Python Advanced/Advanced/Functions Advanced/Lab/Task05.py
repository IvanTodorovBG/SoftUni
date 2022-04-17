def operate(operator, *numbers):
    answer = None
    if operator == "+":
        answer = sum(numbers)

    elif operator == "-":
        current_answer = numbers[0]
        for num in numbers[1:]:
            current_answer -= num
        answer = current_answer

    elif operator == "*":
        answer = 1
        for num in numbers:
            answer *= num

    elif operator == "/":
        current_answer = numbers[0]
        for num in numbers[1:]:
            if num != 0:
                current_answer /= num
        answer = current_answer
    return answer


print(operate("-", 1, 2, 3))
print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 10, 2))
