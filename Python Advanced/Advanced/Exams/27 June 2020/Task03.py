from collections import deque


def list_manipulator(numbers, order, *commands):
    numbers = deque(numbers)
    if order == "add":
        if commands[0] == "beginning":
            for num in commands[:0:-1]:
                numbers.appendleft(num)

        elif commands[0] == "end":
            for num in commands[1:]:
                numbers.append(num)

    elif order == "remove":
        if commands[0] == "beginning":
            if commands[1:]:
                for num in commands[1:]:
                    for _ in range(num):
                        numbers.popleft()
            else:
                numbers.popleft()

        elif commands[0] == "end":
            if commands[1:]:
                for num in commands[1:]:
                    for _ in range(num):
                        numbers.pop()
            else:
                numbers.pop()
    return list(numbers)




