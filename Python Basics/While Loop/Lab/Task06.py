x = input()
import sys
max_num = -sys.maxsize

while x != "Stop":
    number = int(x)
    if number > max_num:
        max_num = number
    x = input()

print(max_num)
