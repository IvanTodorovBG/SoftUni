first_nums = set([int(num) for num in input().split()])
second_nums = set([int(num) for num in input().split()])

n = int(input())

for _ in range(n):

    command = input()

    if "Add First" in command:
        command = command.split()
        for el in command:
            if el.isdigit():
                first_nums.add(int(el))
    elif "Add Second" in command:
        command = command.split()
        for el in command:
            if el.isdigit():
                second_nums.add(int(el))
    elif "Remove First" in command:
        command = command.split()
        for el in command:
            if el.isdigit():
                first_nums.discard(int(el))
    elif "Remove Second" in command:
        command = command.split()
        for el in command:
            if el.isdigit():
                second_nums.discard(int(el))
    elif "Check Subset" in command:
        check_subset_first = first_nums.issubset(second_nums)
        check_subset_second = second_nums.issubset(first_nums)
        if check_subset_first or check_subset_second:
            print("True")
        else:
            print("False")

sorted_first_nums = sorted(first_nums)
print(', '.join([str(num) for num in sorted_first_nums]))
sorted_second_nums = sorted(second_nums)
print(', '.join([str(num) for num in sorted_second_nums]))

