def start_spring(**kwargs):
    collection_spring_objects = {}
    for name_object, type_object in kwargs.items():
        collection_spring_objects.setdefault(type_object, []).append(name_object)

    for key in collection_spring_objects:
        collection_spring_objects[key] = sorted(collection_spring_objects[key])

    collection_spring_objects = dict(sorted(collection_spring_objects.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    answer = []
    for k, v in collection_spring_objects.items():
        answer.append(f'{k}:')
        for item in v:
            answer.append(f'-{item}')
    return '\n'.join(answer)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
