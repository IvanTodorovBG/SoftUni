key = input()
command = input()

while command != "Reveal":
    command = command.split(":|:")
    order = command[0]

    if order == "InsertSpace":
        index = int(command[1])
        key = key[:index] + " " + key[index:]
        print(key)

    elif order == "Reverse":
        substring = command[1]
        if substring in key:
            key = key.replace(substring, "", 1)
            substring = substring[::-1]
            key = key + substring
            print(key)
        else:
            print("error")

    elif order == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        key = key.replace(substring, replacement)
        print(key)

    command = input()

print(f"You have a new text message: {key}")
