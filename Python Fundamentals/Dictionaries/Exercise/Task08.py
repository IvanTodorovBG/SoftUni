command = input()
all_students = {}

while command != "end":
    command = command.split(" : ")
    course = command[0]
    student = command[1]
    all_students.setdefault(course, []).append(student)
    command = input()

sorted_all_students = dict(sorted(all_students.items(), key=lambda x: -len(x[1])))

for key, value in sorted_all_students.items():
    print(f"{key}: {len(value)}")
    print('\n'.join(f"-- {v}" for v in sorted(value)))
