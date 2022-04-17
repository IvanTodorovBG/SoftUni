n = int(input())
chemical_elements = set()

for _ in range(n):

    element = input().split()
    for el in element:
        chemical_elements.add(el)

for unique_chemicals in chemical_elements:
    print(unique_chemicals)
