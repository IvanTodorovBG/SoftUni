initial_energy = int(input())
command = input()

won_battle = 0
lost_game = False

while command != "End of battle":

    distance = int(command)

    if initial_energy >= distance:
        initial_energy -= distance
        won_battle += 1
        if won_battle % 3 == 0:
            initial_energy += won_battle
    else:
        print(f"Not enough energy! Game ends with {won_battle} won battles and {initial_energy} energy")
        lost_game = True
        break

    command = input()

if not lost_game:
    print(f"Won battles: {won_battle}. Energy left: {initial_energy}")