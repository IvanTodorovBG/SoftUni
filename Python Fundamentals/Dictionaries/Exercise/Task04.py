command = input()
phonebook = {}

while not command.isdigit():

    command = command.split("-")
    key = command[0]
    value = command[1]
    phonebook[key] = value

    command = input()

for index in range(int(command)):
    search = input()

    if search in phonebook:
        print(f"{search} -> {phonebook[search]}")
    else:
        print(f"Contact {search} does not exist.")
