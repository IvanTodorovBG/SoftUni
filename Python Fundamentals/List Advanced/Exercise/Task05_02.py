rooms = int(input())

free_chairs = 0
game_on = True

for current_room in range(1, rooms + 1):

    command = input().split()
    chairs = len(command[0])
    visitors = int(command[1])

    if chairs > visitors:
        free_chairs += chairs - visitors
    elif chairs < visitors:
        needed_chairs_in_room = visitors - chairs
        print(f"{needed_chairs_in_room} more chairs needed in room {current_room}")
        game_on = False

if game_on:
    print(f"Game On, {free_chairs} free chairs left")
