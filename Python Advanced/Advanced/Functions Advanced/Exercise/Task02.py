def odd_even(command, *numbers):
    answer = 0
    length_numbs = len([num for nums in numbers for num in nums])
    if command == "Odd":
        answer = sum([num for nums in numbers for num in nums if num % 2 != 0]) * length_numbs
    elif command == "Even":
        answer = sum([num for nums in numbers for num in nums if num % 2 == 0]) * length_numbs
    return answer


print(odd_even(input(), [int(el) for el in input().split()]))
