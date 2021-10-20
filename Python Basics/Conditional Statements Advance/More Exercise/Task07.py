season = input()
group_type = input()
students_count = int(input())
days_count = int(input())

hotel_price = 0
type_sport = ""
total_price = 0

if season == "Winter":
    if group_type == "boys":
        hotel_price = 9.6
        type_sport = "Judo"
    elif group_type == "girls":
        hotel_price = 9.6
        type_sport = "Gymnastics"
    elif group_type == "mixed":
        hotel_price = 10
        type_sport = "Ski"
elif season == "Spring":
    if group_type == "boys":
        hotel_price = 7.2
        type_sport = "Tennis"
    elif group_type == "girls":
        hotel_price = 7.2
        type_sport = "Athletics"
    elif group_type == "mixed":
        hotel_price = 9.5
        type_sport = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        hotel_price = 15
        type_sport = "Football"
    elif group_type == "girls":
        hotel_price = 15
        type_sport = "Volleyball"
    elif group_type == "mixed":
        hotel_price = 20
        type_sport = "Swimming"

total_price = ((students_count * hotel_price) * days_count)

if 10 <= students_count < 20:
    total_price *= 0.95
elif 20 <= students_count < 50:
    total_price *= 0.85
elif students_count >= 50:
    total_price *= 0.5

print(f"{type_sport} {total_price:.2f} lv.")