i = int(input())
bonus = 0

if i <= 100:
    bonus = 5
elif 100 < i <= 1000:
    bonus = i * 0.2
elif i > 1000:
    bonus = i * 0.1

if i % 2 == 0:
    bonus = bonus + 1
elif i % 5 == 0:
    bonus = bonus + 2

print(bonus)
print(bonus + i)