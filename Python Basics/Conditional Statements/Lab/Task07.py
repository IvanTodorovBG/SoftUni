figure = str(input())
if figure == "square":
    a = float(input())
    print(a * a)
elif figure == "rectangle":
    x = float(input())
    y = float(input())
    print(x * y)
elif figure == "circle":
    from math import pi
    r = float(input())
    print(pi * r * r)
elif figure == "triangle":
    b = float(input())
    h = float(input())
    print((b * h) / 2)