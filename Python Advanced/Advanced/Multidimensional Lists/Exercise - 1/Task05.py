rows, columns = [int(num) for num in input().split()]

for row in range(rows):
    for column in range(columns):
        palindrome = f"{chr(97 + row)}{chr(97 + column + row)}{chr(97 + row)}"
        print(palindrome, end=" ")
    print()
