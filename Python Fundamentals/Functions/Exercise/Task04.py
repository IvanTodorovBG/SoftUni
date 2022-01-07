numbers = [int(x) for x in list(input())]


def odd_and_even_sum():

    even_sum = 0
    odd_sum = 0

    for current_number in numbers:
        if current_number % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


odd_and_even_sum()
