command = input()

while command != "end":

    reverse_string = command[::-1]
    print(f"{command} = {reverse_string}")

    command = input()