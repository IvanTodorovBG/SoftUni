count_floors = int(input())
count_rooms = int(input())

for floors in range(count_floors, 0, -1):
    for rooms in range(0, count_rooms):
       if floors == count_floors:
           print(f"L{floors}{rooms}", end=" ")
       elif floors % 2 == 0:
           print(f"O{floors}{rooms}", end=" ")
       else:
           print(f"A{floors}{rooms}", end=" ")
    print()