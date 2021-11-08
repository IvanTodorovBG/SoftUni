width = int(input())
length = int(input())
pieces = input()
total_pieces = width * length
count_pieces = 0
while pieces != "STOP":
    pieces = int(pieces)
    count_pieces += pieces
    if count_pieces > total_pieces:
        not_enough = count_pieces - total_pieces
        print(f"No more cake left! You need {not_enough} pieces more.")
        break
    pieces = input()
if pieces == "STOP":
    if total_pieces > count_pieces:
        enough = total_pieces - count_pieces
        print(f"{enough} pieces are left.")
