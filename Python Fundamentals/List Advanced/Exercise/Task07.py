numbers = [int(i) for i in input().split(", ")]

n = 1
group_range = max(numbers) // 10
group_range_left = max(numbers) % 10

if group_range_left != 0:
    n = 2

for current_group in range(1, group_range + n):
    factor = current_group * 10
    old_factor = (current_group - 1) * 10
    filtered_num = list(filter((lambda x: old_factor < x <= factor), numbers))
    print(f"Group of {factor}'s: {filtered_num}")
