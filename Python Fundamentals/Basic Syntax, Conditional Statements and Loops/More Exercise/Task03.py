year = int(input())
current_year = year
while True:
    current_year += 1
    if len(str(year)) == len(set(str(current_year))):
        print(current_year)
        break
