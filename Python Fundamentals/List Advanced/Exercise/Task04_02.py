numbers = [int(i) for i in input().split(", ")]

print("Positive: {}".format(", ".join([str(i) for i in numbers if i >= 0])))
print("Negative: {}".format(", ".join([str(i) for i in numbers if i < 0])))
print("Even: {}".format(", ".join([str(i) for i in numbers if i % 2 == 0])))
print("Odd: {}".format(", ".join([str(i) for i in numbers if i % 2 != 0])))
