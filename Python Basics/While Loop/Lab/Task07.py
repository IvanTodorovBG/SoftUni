x = input()
import sys
min_num = sys.maxsize

while x != "Stop":
    number = int(x)
    if number < min_num:
        min_num = number
    x = input()

print(min_num)
