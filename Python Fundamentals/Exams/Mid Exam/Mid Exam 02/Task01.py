student_one = int(input())
student_two = int(input())
student_three = int(input())
students_count = int(input())

students_per_hour = student_one + student_two + student_three

working_hours = 0


while True:

    if students_count <= 0:
        print(f"Time needed: {working_hours}h.")
        break
    else:
        working_hours += 1

    if working_hours % 4 == 0:
        continue
    else:
        students_count -= students_per_hour


