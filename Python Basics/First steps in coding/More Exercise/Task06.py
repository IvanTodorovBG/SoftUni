mackerel_price = float(input())
toy_price = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
shells_kg = float(input())
shells_price = 7.5
bonito_price = mackerel_price + (mackerel_price * 0.6)
horse_mackerel_price = toy_price + (toy_price * 0.8)
total_price = (shells_price * shells_kg) + (bonito_price * bonito_kg) \
    + (horse_mackerel_price * horse_mackerel_kg)
print(f"{total_price:.2f}")