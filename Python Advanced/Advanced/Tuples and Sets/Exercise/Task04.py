symbol = input()
unique_symbol = set(symbol)

for char in sorted(unique_symbol):
    print(f"{char}: {symbol.count(char)} time/s")