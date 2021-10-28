n = int(input())

minivan_price = 200
truck_price = 175
train_price = 120
total_load = 0
minivan_price_load = 0
truck_price_load = 0
train_price_load = 0
mid_range_price_load = 0
minivan_load = 0
truck_load = 0
train_load = 0

for i in range(1, n + 1):
    load = int(input())
    total_load += load
    if load <= 3:
        minivan_load += load
        minivan_price_load += load * minivan_price
    elif 4 <= load <= 11:
        truck_load += load
        truck_price_load += load * truck_price
    elif load >= 12:
        train_load += load
        train_price_load += load * train_price

mid_range_price_load = (minivan_price_load + train_price_load + truck_price_load) / total_load
minivan_load_perc = (minivan_load / total_load) * 100
truck_load_perc = (truck_load / total_load) * 100
train_load_perc = (train_load / total_load) * 100

print(f"{mid_range_price_load:.2f}")
print(f"{minivan_load_perc:.2f}%")
print(f"{truck_load_perc:.2f}%")
print(f"{train_load_perc:.2f}%")