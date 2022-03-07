key = [int(i) for i in input().split()]

info = input()
while info != "find":
    # find the message
    new_string = ""
    idx = 0
    for letter in info:
        new_letter = chr(ord(letter) - key[idx])
        new_string += new_letter

        idx += 1
        if idx == len(key):
            idx = 0

    # find type of treasure
    type_treasure = ""
    treasure_found = False
    for el in new_string:
        if treasure_found is False and el == "&":
            treasure_found = True
        elif treasure_found and el != "&":
            type_treasure += el
        elif treasure_found and el == "&":
            break

    # find coordinates
    coordinates = ""
    coordinates_found = False
    for el in new_string:
        if coordinates_found is False and el == "<":
            coordinates_found = True
        elif coordinates_found and el != ">":
            coordinates += el
        elif coordinates_found and el == ">":
            break

    print(f"Found {type_treasure} at {coordinates}")
    info = input()