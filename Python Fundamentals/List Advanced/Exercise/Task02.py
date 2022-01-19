version = [int(i) for i in input().split(".")]

n1 = version[0]
n2 = version[1]
n3 = version[2]

if n3 == 9:
    n3 = 0
    if n2 == 9:
        n2 = 0
        n1 += 1
    else:
        n2 += 1
else:
    n3 += 1

new_version = f"{n1}.{n2}.{n3}"

print(new_version)
