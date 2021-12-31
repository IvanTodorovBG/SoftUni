numbers = [int(i) for i in input().split(" ")]
command = input()


while command != "end":
    command = command.split(" ")
    order = command[0]

    if order == "exchange":
        index = int(command[1])
        if 0 <= index < len(numbers):
            left_side = numbers[index + 1:]
            right_side = numbers[:index + 1]
            numbers = left_side + right_side
        else:
            print("Invalid index")

    elif order == "max":
        element = command[1]

        if element == "odd":
            max_odd_list = [i for i in numbers if i % 2 != 0]
            if not max_odd_list:
                print("No matches")
            else:
                max_odd_number = max(max_odd_list)
                max_odd_index = [idx for idx, num in enumerate(numbers) if num == max_odd_number]
                print(max_odd_index[-1])

        elif element == "even":
            max_even_list = [i for i in numbers if i % 2 == 0]
            if not max_even_list:
                print("No matches")
            else:
                max_even_number = max(max_even_list)
                max_even_index = [idx for idx, num in enumerate(numbers) if num == max_even_number]
                print(max_even_index[-1])

    elif order == "min":
        element = command[1]
        if element == "odd":
            min_odd_list = [i for i in numbers if i % 2 != 0]
            if not min_odd_list:
                print("No matches")
            else:
                min_odd_number = min(min_odd_list)
                min_odd_index = [idx for idx, num in enumerate(numbers) if num == min_odd_number]
                print(min_odd_index[-1])
        elif element == "even":
            min_even_list = [i for i in numbers if i % 2 == 0]
            if not min_even_list:
                print("No matches")
            else:
                min_even_number = min(min_even_list)
                min_even_index = [idx for idx, num in enumerate(numbers) if num == min_even_number]
                print(min_even_index[-1])

    elif order == "first":
        count = int(command[1])
        element = command[2]
        if count > len(numbers):
            print("Invalid count")
        else:
            if element == "even":
                even_list = [i for i in numbers if i % 2 == 0]
                if not even_list:
                    print(even_list)
                else:
                    first_even_list = even_list[:count]
                    print(first_even_list)

            elif element == "odd":
                odd_list = [i for i in numbers if i % 2 != 0]
                if not odd_list:
                    print(odd_list)
                else:
                    first_odd_list = odd_list[:count]
                    print(first_odd_list)

    elif order == "last":
        count = int(command[1])
        element = command[2]
        if count > len(numbers):
            print("Invalid count")
        else:
            if element == "even":
                even_list = [i for i in numbers if i % 2 == 0]
                if not even_list:
                    print(even_list)
                else:
                    last_even_list = even_list[-count:]
                    print(last_even_list)
            elif element == "odd":
                odd_list = [i for i in numbers if i % 2 != 0]
                if not odd_list:
                    print(odd_list)
                else:
                    last_odd_list = odd_list[-count:]
                    print(last_odd_list)

    command = input()

print(numbers)



