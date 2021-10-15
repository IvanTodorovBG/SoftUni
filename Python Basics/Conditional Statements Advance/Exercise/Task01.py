screening_type = input()
rows = int(input())
columns = int(input())

premiere_price = 12
normal_price = 7.5
discount_price = 5

if screening_type == "Premiere":
    total_price = (rows * columns) * premiere_price
    print(f"{total_price:.2f} leva")
elif screening_type == "Normal":
    total_price = (rows * columns) * normal_price
    print(f"{total_price:.2f} leva")
elif screening_type == "Discount":
    total_price = (rows * columns) * discount_price
    print(f"{total_price:.2f} leva")