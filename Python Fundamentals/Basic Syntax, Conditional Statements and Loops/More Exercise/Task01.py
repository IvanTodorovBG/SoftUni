number = input()

number_as_list = list(number)
number_as_list.sort(reverse=True)
final_number = "".join(number_as_list)
print(final_number)