n = int(input())

open = False
close = False
unbalanced = False

for x in range(n):

    command = input()

    if command == "(":
        if open is True:
            print(f"UNBALANCED")
            unbalanced = True
            break
        open = True
        continue

    if command == ")":
        if open is True:
            open = False
            continue
        else:
            print("UNBALANCED")
            unbalanced = True
            break

if unbalanced is False:
    print("BALANCED")




