people = int(input())
capacity = int(input())

courses = people / capacity
extra_course = people % capacity

if extra_course != 0:
    extra_course = 1

print(int(courses + extra_course))