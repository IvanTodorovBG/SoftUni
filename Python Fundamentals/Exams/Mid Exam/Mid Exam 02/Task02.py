numbers = [int(i) for i in input().split(" ")]
command = input()

while command != "end":

    command = command.split(" ")

    order = command[0]

    if order == "swap":
        index_one = int(command[1])
        index_two = int(command[2])

        numbers[index_one], numbers[index_two] = numbers[index_two], numbers[index_one]

    elif order == "multiply":
        index_one = int(command[1])
        index_two = int(command[2])

        numbers[index_one] = numbers[index_one] * numbers[index_two]

    elif order == "decrease":

        for index, number in enumerate(numbers):
            numbers[index] -= 1

    command = input()

print(", ".join([str(x) for x in numbers]))
