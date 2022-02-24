all_contests = {}
all_students = {}
collection_total_points = {}

# collect info fot contests - pass
info = input()
while info != "end of contests":
    contest, password = info.split(":")
    all_contests[contest] = password

    info = input()

student_info = input()
while student_info != "end of submissions":
    student_info = student_info.split("=>")
    contest = student_info[0]
    student_pass = student_info[1]
    username = student_info[2]
    points = int(student_info[3])

    # check for valid contest
    if contest in all_contests and student_pass == all_contests[contest]:
        # collect  student info in dict
        if username not in all_students:
            all_students[username] = {}
            all_students[username][contest] = points
        else:
            if contest not in all_students[username]:
                all_students[username][contest] = points
            else:
                if points > all_students[username][contest]:
                    all_students[username][contest] = points

    student_info = input()

# create student -> total points dict
for student, dicts in all_students.items():
    total_points = sum(dicts.values())
    collection_total_points[student] = total_points

sorted_total_points = dict(sorted(collection_total_points.items(),key=lambda kvp: -kvp[1]))
sorted_all_students = dict(sorted(all_students.items(),key=lambda kvp: kvp[0]))

print(f"Best candidate is {list(sorted_total_points.keys())[0]} with total {list(sorted_total_points.values())[0]} points.")
print("Ranking:")
for current_student in sorted_all_students:
    sorted_d = dict(sorted(sorted_all_students[current_student].items(), key=lambda kvp: kvp[1], reverse=True))
    print(current_student)
    print("\n".join([f'#  {k} -> {v}' for k, v in sorted_d.items()]))