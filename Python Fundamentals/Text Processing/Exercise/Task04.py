text = input()
result = ""

for ch in text:
    result += chr(ord(ch) + 3)

print(result)