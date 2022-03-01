text = input().split(" ")
result = 0
first_part = text[0]
second_part = text[1]

if len(first_part) > len(second_part):

    length = len(first_part) - len(second_part)

    for index in range(len(second_part)):
        result += ord(first_part[index]) * ord(second_part[index])
    remain = first_part[-length:]

    for ch in remain:
        result += ord(ch)

elif len(first_part) < len(second_part):

    length = len(second_part) - len(first_part)

    for index in range(len(first_part)):
        result += ord(first_part[index]) * ord(second_part[index])
    remain = second_part[-length:]

    for ch in remain:
        result += ord(ch)

else:

    for index in range(len(first_part)):
        result += ord(first_part[index]) * ord(second_part[index])

print(result)
