record = float(input())
distance = float(input())
time_per_distance = float(input())
resistance = distance // 15
penalty = resistance * 12.5
total_time = (distance * time_per_distance) + penalty
if total_time < record:
    win_time = record - total_time
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    not_enough_time = total_time - record
    print(f"No, he failed! He was {not_enough_time:.2f} seconds slower.")