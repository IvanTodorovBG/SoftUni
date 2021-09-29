x = float(input())
y = float(input())
h = float(input())

door = 2 * 1.2
windows = 2 * (1.5 * 1.5)
green_one = (2 * (x * x) - door)
green_two = (2 * (x * y) - windows)
total_green = green_one + green_two
green_paint = total_green / 3.4
print("%.2f" % green_paint)

red_one = 2 * (x * y)
red_two = 2 * (x * h / 2)
total_red = red_one + red_two
red_paint = total_red / 4.3
print("%.2f" % red_paint)
