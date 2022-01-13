num = int(input())


def tribonacci(n):
    trib = []

    for i in range(n):
        if i == 0 or i == 1:
            trib.append(1)
        elif i == 2:
            trib.append(2)
        else:
            trib.append(trib[-1] + trib[-2] + trib[-3])

    return " ".join([str(i) for i in trib])


print(tribonacci(num))