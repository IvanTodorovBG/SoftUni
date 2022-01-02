def numbers(number_list):
    num = [abs(float(x)) for x in number_list]
    return num


print(numbers(input().split(" ")))
