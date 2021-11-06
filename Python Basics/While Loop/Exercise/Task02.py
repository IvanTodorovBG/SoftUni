unsatisfied_scores = int(input())
name_problem = input()

total_score = 0
number_problems = 0
last_problem = ""
poor_score = 0

while name_problem != "Enough":
    last_problem = name_problem
    number_problems += 1
    score = int(input())
    total_score += score
    if score <= 4:
        poor_score += 1
    if poor_score == unsatisfied_scores:
        print(f"You need a break, {poor_score} poor grades.")
        break
    name_problem = input()
if name_problem == "Enough":
    average_score = total_score / number_problems
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_problems}")
    print(f"Last problem: {last_problem}")

