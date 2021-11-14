movie_name = input()
standard = 0
student = 0
kid = 0
total_tickets = 0
while movie_name != "Finish":
    empty_space = int(input())
    type = input()
    tickets = 0
    while type != "End":
        total_tickets += 1
        tickets += 1
        if type == "student":
            student += 1
        elif type == "standard":
            standard += 1
        elif type == "kid":
            kid += 1
        if tickets >= empty_space:
            break
        type = input()
    print(f"{movie_name} - {tickets / empty_space * 100:.2f}% full.")
    movie_name = input()
print(f"Total tickets: {total_tickets}")
print(f"{student / total_tickets * 100:.2f}% student tickets.")
print(f"{standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid / total_tickets * 100:.2f}% kids tickets.")

