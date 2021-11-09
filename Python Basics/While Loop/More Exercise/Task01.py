detergent = int(input()) * 750
n = input()
dishes = 0
pots = 0
count = 0

while n != "End":
    dishes_pots = int(n)
    count += 1
    if count % 3 == 0:
        pots += dishes_pots
    elif count % 3 != 0:
        dishes += dishes_pots
    used_detergent = (dishes * 5) + (pots * 15)
    if used_detergent > detergent:
        not_enough = used_detergent - detergent
        print(f"Not enough detergent, {not_enough} ml. more necessary!")
        break
    n = input()
if n == "End":
    enough = detergent - used_detergent
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {enough} ml.")


