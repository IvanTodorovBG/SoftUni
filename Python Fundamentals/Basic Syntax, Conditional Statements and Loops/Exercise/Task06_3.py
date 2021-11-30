year = int(input())
next_year = year + 1
found_happy_year = False
happy_year = ""

while found_happy_year == False:

    next_year_as_str = str(next_year)

    for i in range(len(next_year_as_str)):
        if next_year_as_str[i] not in happy_year:
            happy_year += next_year_as_str[i]

        if len(str(happy_year)) == len(next_year_as_str):
            found_happy_year = True
            break
    if found_happy_year:
        break

    happy_year = ""
    next_year += 1

print(happy_year)
