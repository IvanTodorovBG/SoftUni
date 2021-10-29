n = int(input())

students_bellow_3 = 0
students_3_4 = 0
students_4_5 = 0
students_above_5 = 0
all_student_scores = 0

for i in range(1, n + 1):
    student_score = float(input())
    all_student_scores += student_score
    if 2.00 <= student_score <= 2.99:
        students_bellow_3 += 1
    elif 3.00 <= student_score <= 3.99:
        students_3_4 += 1
    elif 4.00 <= student_score <= 4.99:
        students_4_5 += 1
    elif student_score >= 5.00:
        students_above_5 += 1

students_above_5_perc = students_above_5 / n * 100
students_4_5_perc = students_4_5 / n * 100
students_3_4_perc = students_3_4 / n * 100
students_bellow_3_perc = students_bellow_3 / n * 100
average_score = all_student_scores / n

print(f"Top students: {students_above_5_perc:.2f}%")
print(f"Between 4.00 and 4.99: {students_4_5_perc:.2f}%")
print(f"Between 3.00 and 3.99: {students_3_4_perc:.2f}%")
print(f"Fail: {students_bellow_3_perc:.2f}%")
print(f"Average: {average_score:.2f}")