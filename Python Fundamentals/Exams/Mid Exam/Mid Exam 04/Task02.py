shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":

    command = command.split(" ")

    if command[0] == "Unnecessary":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
    if command[0] == "Urgent":
        if command[1] not in shopping_list:
            shopping_list.insert(0, command[1])
    if command[0] == "Correct":
        if command[1] in shopping_list:
            search_index = shopping_list.index(command[1])
            shopping_list[search_index] = command[2]
    if command[0] == "Rearrange":
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
            shopping_list.append(command[1])

    command = input()

print(", ".join(shopping_list))