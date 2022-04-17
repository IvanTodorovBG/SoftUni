def numbers_searching(*args):
    answer = []
    duplicate_nums = []
    min_num, max_num = min(args), max(args)
    for search_num in range(min_num, max_num + 1):
        if search_num not in args:
            answer.append(search_num)
    for number in set(args):
        if args.count(number) > 1:
            duplicate_nums.append(number)
    answer.append(sorted(duplicate_nums))
    return answer


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))