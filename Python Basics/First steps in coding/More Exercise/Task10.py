degree = float(input())

if 5.00 <= degree <= 11.9:
    print("Cold")
elif 12.00 <= degree <= 14.9:
    print("Cool")
elif 15.00 <= degree <= 20.00:
    print("Mild")
elif 20.1 <= degree <= 25.9:
    print("Warm")
elif 26.00 <= degree <= 35.00:
    print("Hot")
else:
    print("unknown")