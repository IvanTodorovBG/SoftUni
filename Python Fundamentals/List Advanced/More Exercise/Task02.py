string = input()
num_list = [int(i) for i in string if i.isdigit()]

take_numbers = num_list[::2]
skip_numbers = num_list[1::2]

string_list = [str(i) for i in string if not i.isdigit()]

take_list = []
skip_list = []

for index in range(len(take_numbers)):

    take = take_numbers[index]
    skip = skip_numbers[index]

    take_list += string_list[:take]
    del string_list[:take]

    skip_list += string_list[:skip]
    del string_list[:skip]

print("".join([str(x) for x in take_list]))


