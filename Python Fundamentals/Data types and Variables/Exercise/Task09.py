n = int(input())

value = 0
max_value = 0
max_quality = 0
max_weight = 0
max_time = 0

for x in range(n):

    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight / time_needed) ** quality

    if value > max_value:
        max_value = value
        max_quality = quality
        max_time = time_needed
        max_weight = weight

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")
