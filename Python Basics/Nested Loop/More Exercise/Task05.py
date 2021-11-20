male = int(input())
female = int(input())
table = int(input())
count_seats = 0
for man in range(1, male + 1):
    for woman in range(1, female + 1):
        count_seats += 1
        if count_seats == table:
            print(f"({man} <-> {woman})", end=" ")
            break
        print(f"({man} <-> {woman})", end=" ")
    if count_seats == table:
        break


