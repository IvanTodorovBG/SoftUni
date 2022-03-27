numbers = [int(x) for x in input().split(" ")]

average_numbers = int(round(sum(numbers) / len(numbers)))

final_list = list(filter(lambda x: x > average_numbers, numbers))

final_list.sort(reverse=True)

final_sorted_list = final_list[:5]

if not final_sorted_list:
    print("No")
else:
    print(" ".join([str(x) for x in final_sorted_list]))
