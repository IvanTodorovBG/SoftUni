text = list(input())
stack = []

for _ in range(len(text)):
    stack.append(text.pop())

print("".join(stack))