data = open("numbers.txt").read().split("\n")
print(sum([int(num) for num in data]))