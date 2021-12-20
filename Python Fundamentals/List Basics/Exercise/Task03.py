command = input().split(" ")

team_A = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_B = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
team_A_count = 11
team_B_count = 11
terminated = False

for x in command:
    if x in team_A:
        team_A_count -= 1
        team_A.remove(x)
    if x in team_B:
        team_B_count -= 1
        team_B.remove(x)
    if team_A_count < 7 or team_B_count < 7:
        terminated = True
        break

if terminated:
    print(f"""Team A - {team_A_count}; Team B - {team_B_count}
Game was terminated""")
else:
    print(f"Team A - {team_A_count}; Team B - {team_B_count}")


