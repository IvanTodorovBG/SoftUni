name = input()
grade = 0
bad_score = 0
total_score = 0
average_grade = 0
while True:
    score = float(input())
    total_score += score
    grade += 1
    if score < 4:
        bad_score += 1
    if bad_score == 1:
        print(f"{name} has been excluded at {grade} grade")
        break
    if grade == 12:
        average_grade = total_score / grade
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break

