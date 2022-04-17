n = int(input())
parking_lot = set()

for _ in range(n):

    cars = input().split(", ")
    command, reg_num = cars

    if command == "IN":
        parking_lot.add(reg_num)
    elif command == "OUT":
        if reg_num in parking_lot:
            parking_lot.remove(reg_num)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")