fireworks_effects = [int(x) for x in input().split(", ")]
explosive_power = [int(x) for x in input().split(", ")]
palm_firework = 0
willow_firework = 0
crossette_firework = 0

while True:

    if explosive_power and fireworks_effects:

        if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
            break

        if fireworks_effects[0] <= 0:
            fireworks_effects.pop(0)
            continue
        elif explosive_power[-1] <= 0:
            explosive_power.pop(-1)
            continue

        explosion = fireworks_effects[0] + explosive_power[-1]

        if explosion % 3 == 0 and explosion % 5 != 0:
            palm_firework += 1
            fireworks_effects.pop(0)
            explosive_power.pop(-1)
        elif explosion % 5 == 0 and explosion % 3 != 0:
            willow_firework += 1
            fireworks_effects.pop(0)
            explosive_power.pop(-1)
        elif explosion % 3 == 0 and explosion % 5 == 0:
            crossette_firework += 1
            fireworks_effects.pop(0)
            explosive_power.pop(-1)
        else:
            fireworks_effects[0] -= 1
            fireworks_effects.append(fireworks_effects.pop(0))

    else:
        break

if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")
