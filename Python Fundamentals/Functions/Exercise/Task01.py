num_one = int(input())
num_two = int(input())
num_three = int(input())


def smallest_number(a, b, c):
    min_num = None
    if a <= b and a <= c:
        min_num = a
    elif b <= a and b <= c:
        min_num = b
    else:
        min_num = c
    return min_num


print(smallest_number(num_one, num_two, num_three))
