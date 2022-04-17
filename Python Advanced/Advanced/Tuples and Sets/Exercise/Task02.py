lengths = input().split()
n, m = lengths
length_n = set()
length_m = set()

for _ in range(int(n)):

    command = int(input())
    length_n.add(command)

for _ in range(int(m)):

    element = int(input())
    length_m.add(element)

intersection = length_n.intersection(length_m)

for num in intersection:
    print(num)