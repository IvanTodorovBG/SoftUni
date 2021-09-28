w = float(input())
h = float(input())
h = h * 100
w = w * 100
h -= 100
desks = (h // 70)
lines = (w // 120)
total_seats = (desks * lines) - 3
print(int(total_seats))