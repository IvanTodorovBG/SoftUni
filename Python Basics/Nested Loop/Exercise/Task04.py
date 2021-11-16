n = int(input())
presentation = input()
final_score = 0
count = 0
while presentation != "Finish":
    total_score = 0
    for a in range(1, n + 1):
        score = float(input())
        total_score += score
        final_score += score
        count += 1
    print(f"{presentation} - {total_score / a:.2f}.")
    presentation = input()
if presentation == "Finish":
    print(f"Student\'s final assessment is {final_score / count:.2f}.")

