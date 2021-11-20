last_sector = (input())
count_lines = int(input())
count_seats = int(input())
count1 = 1
count2 = 0
count_combination = 0
for a in range(ord("A"), ord(last_sector) + 1):
    count1 += 0
    count2 += 1
    if count2 > count1:
        count_lines += 1
    for b in range(1, count_lines + 1):
        if b % 2 != 0:
            for c in range(97, (97 + count_seats)):
                count_combination += 1
                print(f"{chr(a)}{b}{chr(c)}", end=" ")
                print()
        else:
            for c in range(97, (97 + (count_seats+2))):
                count_combination += 1
                print(f"{chr(a)}{b}{chr(c)}", end=" ")
                print()
print(count_combination)

