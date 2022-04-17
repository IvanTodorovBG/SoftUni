n = int(input())
stack = []
rev_stack = []

for _ in range(n):

    numbers = input()

    if "1 " in numbers:
        numbers = numbers.split()
        stack.append(int(numbers[-1]))
    elif numbers == "2":
        if stack:
            stack.pop()
    elif numbers == "3":
        if stack:
            print(max(stack))
    elif numbers == "4":
        if stack:
            print(min(stack))

for _ in range(len(stack)):
    rev_stack.append(stack.pop())

print(", ".join([str(x) for x in rev_stack]))

