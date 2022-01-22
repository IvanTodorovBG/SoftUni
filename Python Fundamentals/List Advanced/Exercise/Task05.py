number_of_rooms = int(input())

free_chairs = 0
no_free_chairs = False

for current_room in range(1, number_of_rooms + 1):

    room = input().split(" ")
    chairs = len(room[0])
    people = int(room[1])

    if chairs < people:
        needed_chairs = people - chairs
        no_free_chairs = True
        print(f"{needed_chairs} more chairs needed in room {current_room}")
    else:
        free_chairs += chairs - people

if not no_free_chairs:
    print(f"Game On, {free_chairs} free chairs left")