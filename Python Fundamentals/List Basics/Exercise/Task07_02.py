def outofstock(names_gifts, gifts):
    names_gifts = [gif.replace(gifts, "None") for gif in names_gifts]
    return names_gifts


def required(names_gifts, gifts, idx):
    names_gifts.pop(idx)
    names_gifts.insert(idx, gifts)
    return names_gifts


def justincase(names_gifts, gifts):
    names_gifts.pop()
    names_gifts.append(gifts)
    return names_gifts


names_of_gifts = input().split(" ")
command = input()

while command != "No Money":

    order = command.split(" ")[0]
    gift = command.split(" ")[1]

    if order == "OutOfStock":
        if gift in names_of_gifts:
            names_of_gifts = outofstock(names_of_gifts, gift)

    elif order == "Required":
        index = int(command.split(" ")[2])

        if 0 <= index < len(names_of_gifts):
            names_of_gifts = required(names_of_gifts, gift, index)

    elif order == "JustInCase":
        names_of_gifts = justincase(names_of_gifts, gift)

    command = input()

answer_list = " ".join([str(x) for x in names_of_gifts if x != "None"])

print(answer_list)