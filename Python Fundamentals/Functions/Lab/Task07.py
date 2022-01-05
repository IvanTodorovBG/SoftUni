def rounding(numbers):
    num = [round(float(x)) for x in numbers]
    return num


print(rounding(input().split(" ")))