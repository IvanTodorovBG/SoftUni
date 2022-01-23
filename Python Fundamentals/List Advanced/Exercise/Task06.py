number_of_electrons = int(input())

n = 1
answer = []

while True:

    max_number_electrons_in_shell = 2 * pow(n, 2)

    if number_of_electrons >= max_number_electrons_in_shell:
        number_of_electrons -= max_number_electrons_in_shell
        answer.append(max_number_electrons_in_shell)
        n += 1
    else:
        if number_of_electrons != 0:
            answer.append(number_of_electrons)
            break
        else:
            break

print(answer)


