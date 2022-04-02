message = input()
command = input()

while command != "Decode":
    command = command.split("|")
    order = command[0]

    if order == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

    elif order == "Move":
        n = int(command[1])
        left_side = message[:n]
        right_side = message[n:]
        message = right_side + left_side

    elif order == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]

    command = input()

print(f"The decrypted message is: {message}")



