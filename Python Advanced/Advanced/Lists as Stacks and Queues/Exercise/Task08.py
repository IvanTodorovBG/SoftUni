from collections import deque

green_window = int(input())
free_window = int(input())

cars = deque()
passed_cars = 0
has_crashed = False

while True:
    line = input()
    if line == "END":
        break

    if line == "green":
        current_green = green_window
        while cars and current_green > 0:
            car = cars.popleft()
            if current_green >= len(car) or current_green + free_window >= len(car):
                passed_cars += 1
                current_green -= len(car)
            else:
                print('A crash happened!')
                print(f'{car} was hit at {car[current_green + free_window]}.')
                has_crashed = True
                break
    else:
        cars.append(line)

    if has_crashed:
        break

if not has_crashed:
    print('Everyone is safe.')
    print(f'{passed_cars} total cars passed the crossroads.')