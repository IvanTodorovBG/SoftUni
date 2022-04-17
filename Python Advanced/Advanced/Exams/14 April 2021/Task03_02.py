def flights(*args):
    plane_dict = {}
    elements = []

    for arg in args:
        if arg == "Finish":
            break
        else:
            elements.append(arg)

    destinations = elements[::2]
    passengers = elements[1::2]

    for index in range(len(destinations)):
        if destinations[index] not in plane_dict:
            plane_dict[destinations[index]] = 0
        plane_dict[destinations[index]] += passengers[index]
    return plane_dict


