employees_happiness = [int(x) for x in input().split()]
improvement_factor = int(input())

for index, employee in enumerate(employees_happiness):
    employees_happiness[index] *= improvement_factor

average = sum(employees_happiness) / len(employees_happiness)

happy_list = []

for employee in employees_happiness:
    if employee >= average:
        happy_list.append(employee)

happy_count = len(happy_list)
total_count = len(employees_happiness)

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")