n = int(input())
students = {}

for _ in range(n):

    command = input().split()
    student, grade = command

    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for name, score in students.items():
    avg = sum(score) / len(score)
    grades = " ".join([f'{num:.2f}' for num in score])
    print(f"{name} -> {grades} (avg: {avg:.2f})")
