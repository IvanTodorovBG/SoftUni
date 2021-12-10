start_range = int(input())
stop_range = int(input())

for x in range(start_range, stop_range + 1):
    print(f"{(chr(x))}", end=" ")