import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def get_distance(num1, num2):
    x = math.pow(num1, 2)
    y = math.pow(num2, 2)
    return math.sqrt(x + y)


double_distance_1 = get_distance(x1, y1)
double_distance_2 = get_distance(x2, y2)

if double_distance_1 <= double_distance_2:
    print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")

else:
    print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")
