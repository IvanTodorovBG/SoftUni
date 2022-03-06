symbol_1 = input()
symbol_2 = input()
string = input()

total_sum = 0
for letter in string:
    if ord(symbol_1) < ord(letter) < ord(symbol_2):
        total_sum += ord(letter)

print(total_sum)