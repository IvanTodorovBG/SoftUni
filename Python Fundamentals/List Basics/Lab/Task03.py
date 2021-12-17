n = int(input())

positive = []
negative = []

for x in range(n):
    numbers = int(input())

    if numbers >= 0:
        positive.append(numbers)
    else:
        negative.append(numbers)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")

