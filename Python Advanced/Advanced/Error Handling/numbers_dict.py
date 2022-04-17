numbers_dictionary = {}

number_as_string = input()

while number_as_string != "Search":
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    number_as_string = input()

searched_number = input()

while searched_number != "Remove":
    try:
        print(numbers_dictionary[searched_number])
    except KeyError:
        print("Number does not exist in dictionary")
    searched_number = input()

num_to_be_del = input()

while num_to_be_del != "End":
    try:
        del numbers_dictionary[num_to_be_del]
    except KeyError:
        print("Number does not exist in dictionary")
    num_to_be_del = input()

print(numbers_dictionary)
