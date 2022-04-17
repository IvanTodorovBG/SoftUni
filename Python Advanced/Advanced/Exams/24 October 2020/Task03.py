from collections import deque


def best_list_pureness(data, k):
    numbers = deque(data)
    best_pureness = 0
    best_rotate = 0
    for current_index in range(k + 1):
        current_pureness = 0
        for index, num in enumerate(numbers):
            current_pureness += num * index
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotate = current_index
        numbers.appendleft(numbers.pop())
    return f"Best pureness {best_pureness} after {best_rotate} rotations"
