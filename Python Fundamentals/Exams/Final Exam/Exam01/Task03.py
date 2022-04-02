piano = {}
n = int(input())

for _ in range(n):
    element = input().split("|")
    piece = element[0]
    composer = element[1]
    key = element[2]

    piano[piece] = [composer, key]

command = input()

while command != "Stop":

    command = command.split("|")
    order = command[0]
    piece = command[1]

    if order == "Add":
        composer = command[2]
        key = command[3]
        if piece not in piano:
            piano[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif order == "Remove":
        if piece in piano:
            del piano[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif order == "ChangeKey":
        new_key = command[2]
        if piece in piano:
            piano[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

sorted_piano = dict(sorted(piano.items(), key=lambda x: (x[0], x[1][0])))

for song, value in sorted_piano.items():
    print(f"{song} -> Composer: {value[0]}, Key: {value[1]}")
