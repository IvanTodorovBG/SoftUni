elements = input().split(" ")

moves = 0
you_won = False
command = input()

while command != "end":
    moves += 1
    command = command.split(" ")
    index_1 = int(command[0])
    index_2 = int(command[1])

# if player is Not cheating!
    if index_1 != index_2 and 0 <= index_1 < len(elements) and 0 <= index_2 < len(elements):

        if elements[index_1] == elements[index_2]:
            print(f"Congrats! You have found matching elements - {elements[index_1]}!")
            new_elements = [item for index, item in enumerate(elements) if index not in (index_1, index_2)]
            elements = new_elements
        else:
            print("Try again!")

# if player Is cheating!
    else:
        print("Invalid input! Adding additional elements to the board")
        middle_index_1 = int(len(elements) / 2)
        middle_index_2 = int(len(elements) / 2) + 1
        new_element = "-" + str(moves) + "a"
        elements.insert(middle_index_1, new_element)
        elements.insert(middle_index_2, new_element)

# if list of elements is empty -> hit all elements
    if not elements:
        you_won = True
        break

    command = input()

if you_won is True:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(elements))