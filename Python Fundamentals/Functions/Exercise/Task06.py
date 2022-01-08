

def sort(numbers):
    list_of_numbers = [int(x) for x in numbers]
    return sorted(list_of_numbers)


print(sort(input().split()))
