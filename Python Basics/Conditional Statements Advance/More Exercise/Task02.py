juniors_count = int(input())
seniors_count = int(input())
race_track = input()

juniors_price = 0
seniors_price = 0
total_racers = juniors_count + seniors_count

if race_track == "trail":
    juniors_price = 5.5
    seniors_price = 7
elif race_track == "cross-country":
    juniors_price = 8
    seniors_price = 9.5
    if total_racers >= 50:
        juniors_price = juniors_price - (juniors_price * 0.25)
        seniors_price = seniors_price - (seniors_price * 0.25)
elif race_track == "downhill":
    juniors_price = 12.25
    seniors_price = 13.75
elif race_track == "road":
    juniors_price = 20
    seniors_price = 21.5

total_price = ((juniors_price * juniors_count) + (seniors_price * seniors_count)) * 0.95
print("%.2f" % total_price)


