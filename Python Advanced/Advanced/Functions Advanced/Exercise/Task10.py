def fill_the_box(*args):
    box_size = 1
    cubes = args[3:]
    total_cubes = 0
    box_size_hlw = args[:3]
    for size in box_size_hlw:
        box_size *= size
    for cube in cubes:
        if cube == "Finish":
            break
        total_cubes += cube
    if box_size > total_cubes:
        return f"There is free space in the box. You could put {box_size - total_cubes} more cubes."
    return f"No more free space! You have {total_cubes - box_size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))