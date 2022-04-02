n = int(input())
all_pieces = {}
for _ in range(n):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[2]
    if piece not in all_pieces:
        all_pieces[piece] = {}
    all_pieces[piece]['composer'] = composer
    all_pieces[piece]['key'] = key

command = input()

while command != "Stop":

    command = command.split("|")
    order = command[0]
    piece = command[1]

    if order == "Add":
        composer = command[2]
        key = command[3]

        if piece not in all_pieces:
            all_pieces[piece] = {}
            all_pieces[piece]['composer'] = composer
            all_pieces[piece]['key'] = key
            print(f"{piece} by {composer} in {key} added to the collection!")

        else:
            print(f"{piece} is already in the collection!")

    elif order == "Remove":
        if piece in all_pieces:
            del all_pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif order == "ChangeKey":
        new_key = command[2]
        if piece in all_pieces:
            all_pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

sorted_all_piece = dict(sorted(all_pieces.items(), key=lambda kvp: (kvp[0], kvp[1]['composer'])))

for kvp in sorted_all_piece.items():
    print(f"{kvp[0]} -> Composer: {kvp[1]['composer']}, Key: {kvp[1]['key']}")