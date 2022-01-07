def characters_in_range(start, stop):
    letters = []
    for characters in range(ord(start) + 1, ord(stop)):
        letters.append(chr(characters))
    letters_as_string = " ".join(letters)
    return letters_as_string


print(characters_in_range(input(), input()))


