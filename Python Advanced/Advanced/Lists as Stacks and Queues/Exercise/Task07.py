from collections import deque


def add_a_second(hrs, mins, secs):
    secs += 1
    if secs == 60:
        secs = 0
        mins += 1
        if mins == 60:
            mins = 0
            hrs += 1
            if hrs == 24:
                hrs = 0
    return hrs, mins, secs


def add_a_sec_to_robots(robots):
    for current_robot in robots:
        if current_robot[2] < 0:
            current_robot[2] += 1
    return robots


robots_info = input().split(";")
hours, minutes, seconds = [int(i) for i in input().split(":")]

# make list of all robots
all_robots = []
for robot in robots_info:
    robot = robot.split("-")
    name = robot[0]
    working_time = int(robot[1])
    all_robots.append([name, working_time, 0])

# make deque of all products
all_products = deque()
command = input()
while command != "End":
    all_products.append(command)
    command = input()


while all_products:
    product = all_products[0]
    hours, minutes, seconds = add_a_second(hours, minutes, seconds)
    all_robots = add_a_sec_to_robots(all_robots)
    product_is_free = True

    for robot in all_robots:
        name = robot[0]
        working_time = robot[1]
        if robot[2] == 0:
            robot[2] -= working_time
            print(f'{name} - {product} [{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}]')

            product_is_free = False
            break

    if product_is_free is False:
        all_products.popleft()
        continue
    else:
        all_products.append(all_products.popleft())