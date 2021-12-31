line_one = input().split(" ")
line_two = input().split(" ")
line_three = input().split(" ")

we_have_winner = False

for current_line in (line_one, line_two, line_three):
    if current_line[0] == current_line[1] == current_line[2] and current_line[0] != "0":
        if current_line[0] == "1":
            print("First player won")
            we_have_winner = True
            break
        else:
            print("Second player won")
            we_have_winner = True
            break

for current_index in range(0, 3):
    if line_one[current_index] == line_two[current_index] == line_three[current_index] and line_one[current_index] != "0":
        if line_one[current_index] == "1":
            print("First player won")
            we_have_winner = True
            break
        else:
            print("Second player won")
            we_have_winner = True
            break

if line_one[0] == line_two[1] == line_three[2] and line_one[0] != "0":
    if line_one[0] == "1":
        print("First player won")
        we_have_winner = True
    else:
        print("Second player won")
        we_have_winner = True

if line_one[2] == line_two[1] == line_three[0] and line_one[2] != "0":
    if line_one[2] == "1":
        print("First player won")
        we_have_winner = True
    else:
        print("Second player won")
        we_have_winner = True

if not we_have_winner:
    print("Draw!")

