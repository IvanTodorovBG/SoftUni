number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

total_bonus = 0
max_bonus = 0
max_student = 0

for student in range(1, number_of_students + 1):
    student_attendance = int(input())
    total_bonus = student_attendance / number_of_lectures * (5 + additional_bonus)
    if max_bonus < total_bonus:
        max_bonus = total_bonus
        max_student = student_attendance

print(f"""Max Bonus: {round(max_bonus)}.
The student has attended {max_student} lectures.""")
