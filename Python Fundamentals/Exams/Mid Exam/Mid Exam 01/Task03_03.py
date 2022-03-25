def no_match(num):
    mid_index = int(len(num) / 2)
    left_side = num[:mid_index]
    right_side = num[mid_index:]
    item_to_append = f"-{moves}a"
    left_side += [item_to_append] * 2
    print("Invalid input! Adding additional elements to the board")
    return left_side + right_side


def match(num):
    print(f"Congrats! You have found matching elements - {num[match_one]}!")
    unwanted_idx = (match_one, match_two)
    return [item for i, item in enumerate(num) if i not in unwanted_idx]


numbers = input().split(" ")
command = input()

moves = 0
you_won = False

while command != "end":

    command = command.split(" ")
    moves += 1
    match_one = int(command[0])
    match_two = int(command[1])

    if match_one == match_two or not 0 <= match_one < len(numbers) or not 0 <= match_two < len(numbers):
        numbers = no_match(numbers)

    else:
        if numbers[match_one] == numbers[match_two]:
            numbers = match(numbers)

        else:
            print("Try again!")

    if not numbers:
        print(f"You have won in {moves} turns!")
        you_won = True
        break

    command = input()

remain_numbers = " ".join([str(x) for x in numbers])

if not you_won:
    print(f"Sorry you lose :(\n{remain_numbers}")
