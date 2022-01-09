

def min_max_and_sum(numbers):
    list_of_numbers = [int(x) for x in numbers]
    return (f"""The minimum number is {min(list_of_numbers)}
The maximum number is {max(list_of_numbers)}
The sum number is: {sum(list_of_numbers)}""")


print(min_max_and_sum(input().split(" ")))
