command = input()
all_students = {}

while command[0].isupper():

    command = command.split(":")
    key = command[2]
    value = command[0] + " - " + command[1]
    all_students.setdefault(key, []).append(value)
    command = input()

searched_course = command.replace("_", " ")

print("\n".join(all_students[searched_course]))
