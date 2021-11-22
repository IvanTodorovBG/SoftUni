start = int(input())
end = int(input())
magic_number = int(input())

magic_number_found = False
combinations = 0

for number_one in range(start, end + 1):
    for number_two in range(start, end + 1):
        combinations += 1
        if number_one + number_two == magic_number:
            magic_number_found = True
            print(f"Combination N:{combinations} ({number_one} + {number_two} = {magic_number})")
            break
        if magic_number_found:
            break
    if magic_number_found:
        break
else:
    print(f"{combinations} combinations - neither equals {magic_number}")