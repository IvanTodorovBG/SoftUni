start = int(input())
stop = int(input())

for a in range(start, stop + 1):
    even_1 = str(a)[0]
    even_2 = str(a)[2]
    even_3 = str(a)[4]
    even = int(even_1) + int(even_2) + int(even_3)
    odd_1 = str(a)[1]
    odd_2 = str(a)[3]
    odd_3 = str(a)[5]
    odd = int(odd_1) + int(odd_2) + int(odd_3)
    if even == odd:
        print(f"{a}", end=" ")