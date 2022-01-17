employees_happiness = list(map(lambda x: int(x), input().split()))
improvement_factor = int(input())

employee_after_factor = list(map((lambda a: a * improvement_factor), employees_happiness))

average = sum(employee_after_factor) / len(employee_after_factor)

happy_count = len(list(filter((lambda x: x >= average), employee_after_factor)))
total_count = len(employee_after_factor)

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")