start = input()
stop = input()
without = ord(input())
count = 0
for first in range(ord(start), ord(stop) + 1):
    for second in range(ord(start), ord(stop) + 1):
        for third in range(ord(start), ord(stop) + 1):
            if first != without and second != without and third != without:
                count += 1
                print(chr(first) + chr(second) + chr(third), end=" ")
print(count)




