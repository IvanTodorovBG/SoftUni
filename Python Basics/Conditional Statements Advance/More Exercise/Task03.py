hrizantemi_count = int(input())
rozi_count = int(input())
laleta_count = int(input())
season = input()
holiday = input()

hrizantemi_price = 0
rozi_price = 0
laleta_price = 0
total_price = 0

total_count_flowers = laleta_count + rozi_count + hrizantemi_count

if season in ("Spring", "Summer"):
    hrizantemi_price = 2
    rozi_price = 4.1
    laleta_price = 2.5
elif season in ("Autumn", "Winter"):
    hrizantemi_price = 3.75
    rozi_price = 4.5
    laleta_price = 4.15

if holiday == "Y":
    hrizantemi_price = hrizantemi_price + (hrizantemi_price * 0.15)
    rozi_price = rozi_price + (rozi_price * 0.15)
    laleta_price = laleta_price + (laleta_price * 0.15)

total_price = (hrizantemi_price * hrizantemi_count) + (rozi_price * rozi_count) + (laleta_price * laleta_count)

if laleta_count > 7 and season == "Spring":
    total_price = total_price - (total_price * 0.05)

if rozi_count >= 10 and season == "Winter":
    total_price = total_price - (total_price * 0.1)

if total_count_flowers > 20:
    total_price = total_price - (total_price * 0.2)

total_price += 2

print("%.2f" % total_price)