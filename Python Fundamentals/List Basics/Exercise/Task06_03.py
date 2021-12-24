def min_number(nums, count_of_nums):
    for num in range(count_of_nums):
        min_num = min(nums)
        nums.remove(min_num)
    print(", ".join([str(num) for num in numbers]))


numbers = [int(num) for num in input().split(" ")]
count_of_numbers = int(input())


min_number(numbers, count_of_numbers)
