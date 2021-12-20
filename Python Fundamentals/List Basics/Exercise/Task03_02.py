command = input().split(" ")

team_a_count = 11
team_b_count = 11
team_a = []
team_b = []

lost = False

for index in command:
    order = index.split("-")
    team = order[0]
    player = int(order[1])
    if team == "A":
        if player not in team_a:
            team_a.append(player)
            team_a_count -= 1
            if team_a_count < 7:
                lost = True
                break

    else:
        if player not in team_b:
            team_b.append(player)
            team_b_count -= 1
            if team_a_count < 7:
                lost = True
                break

if not lost:
    print(f"Team A - {team_a_count}; Team B - {team_b_count}")
else:
    print(f"Team A - {team_a_count}; Team B - {team_b_count}")
    print("Game was terminated")
