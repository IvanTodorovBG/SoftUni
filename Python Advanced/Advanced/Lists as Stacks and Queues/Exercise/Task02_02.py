n = int(input())
numbers = []

for _ in range(n):

    command = input()

    if command == "2":
        if numbers:
            numbers.pop()

    elif command == "3":
        if numbers:
            print(max(numbers))

    elif command == "4":
        if numbers:
            print(min(numbers))

    else:
        command = command.split()
        numbers.append(int(command[1]))

print(", ".join([str(num) for num in reversed(numbers)]))
