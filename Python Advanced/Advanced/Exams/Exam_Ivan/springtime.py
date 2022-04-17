def make_a_dict_of_objects(**kwargs):
    dictionary = {}
    for name_object, type_object in kwargs.items():
        if type_object not in dictionary:
            dictionary[type_object] = []
        dictionary[type_object].append(name_object)
    return dictionary


def sort_values(objects):
    for k in objects:
        objects[k] = sorted(objects[k])
    return objects


def do_output(objects):
    for_printing = []
    for k, v in objects.items():
        for_printing.append(f'{k}:')
        for el in v:
            for_printing.append(f'-{el}')
    return for_printing


def start_spring(**kwargs):
    spring_objects = make_a_dict_of_objects(**kwargs)
    spring_objects = sort_values(spring_objects)
    spring_objects = dict(sorted(spring_objects.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    output = do_output(spring_objects)

    return '\n'.join(output)

