number_of_students = int(input())
all_students = {}
all_students_high_score = {}

# adding all students + grades in dictionary
for current_student in range(number_of_students):
    student = input()
    grade = float(input())

    all_students.setdefault(student, []).append(grade)

# calculating average grade
for k, v in all_students.items():
    all_students[k] = sum(v) / len(v)

# adding in new dictionary only the high score students
    if all_students[k] >= 4.5:
        all_students_high_score[k] = all_students[k]

# sorting the students
sorted_all_students = dict(sorted(all_students_high_score.items(), key=lambda x: -x[1]))

print("\n".join(f"{key} -> {value:.2f}" for key, value in sorted_all_students.items()))

