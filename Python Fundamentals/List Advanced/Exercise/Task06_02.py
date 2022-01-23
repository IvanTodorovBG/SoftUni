number_of_electrons = int(input())

n = 1
filled_shells = []

while True:

    shell = 2 * (n ** 2)
    if number_of_electrons >= shell:
        filled_shells.append(shell)
        number_of_electrons -= shell
        if number_of_electrons == 0:
            break

    if number_of_electrons < shell:
        filled_shells.append(number_of_electrons)
        break

    n += 1

print(filled_shells)


