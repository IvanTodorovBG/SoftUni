key = int(input())
n = int(input())

message = ""

for x in range(n):
    letters = input()
    message += chr(ord(letters) + key)

print(message)