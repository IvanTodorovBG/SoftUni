def even_odd(*elements):
    answer = []
    numbers = elements[:-1]
    command = elements[-1]
    if command == "even":
        for el in numbers:
            if el % 2 == 0:
                answer.append(el)
    elif command == "odd":
        for num in numbers:
            if num % 2 != 0:
                answer.append(num)
    return answer


