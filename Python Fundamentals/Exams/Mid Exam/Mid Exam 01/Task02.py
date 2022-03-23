people = int(input())
empty_seats = [int(x) for x in input().split(" ")]
counter = 0
no_more_people = False

for index, current_seat in enumerate(empty_seats):
    for seats in range(current_seat, 4):
        if people > 0:
            people -= 1
            counter += 1
        else:
            no_more_people = True
            break
    if counter < 4:
        counter += current_seat

    empty_seats[index] = counter
    counter = 0

new_seats = " ".join([str(x) for x in empty_seats])

if people > 0 and empty_seats[-1] == 4:
    print(f"There isn\'t enough space! {people} people in a queue!")
    print(new_seats)

if people == 0 and empty_seats[-1] == 4:
    print(new_seats)

if no_more_people:
    print(f"The lift has empty spots!")
    print(new_seats)