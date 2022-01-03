def calculator(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = int(a / b)
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


input_operator = input()
first_num = int(input())
second_num = int(input())

print(calculator(first_num, second_num, input_operator))