text = input()
command = input()

while command != "Travel":
    search_command = command[0]

    if search_command == "A" or search_command == "R":
        add_remove_split = command.split(" ")
        order = add_remove_split[0]

        if order == "Add":
            add_remove_split = add_remove_split[1].split(":")
            index = int(add_remove_split[1])
            string = add_remove_split[2]

            if 0 <= index <= len(text):
                text = text[:index] + string + text[index:]
            print(text)

        elif order == "Remove":
            add_remove_split = add_remove_split[1].split(":")
            start_index = int(add_remove_split[1])
            end_index = int(add_remove_split[2])

            if start_index >= 0 and end_index < len(text):
                text = text[:start_index] + text[end_index + 1:]
            print(text)

    elif search_command == "S":
        switch_split = command.split(":")
        old_string = switch_split[1]
        new_string = switch_split[2]

        if old_string in text:
            text = text.replace(old_string, new_string)
        print(text)

    command = input()

print(f"Ready for world tour! Planned stops: {text}")
