command = input()
book = {}
all_sides = {}

while command != "Lumpawaroo":

    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        if force_user not in book:
            book[force_user] = force_side

    elif "->" in command:
        command = command.split(" -> ")
        force_side = command[1]
        force_user = command[0]
        if force_user in book:
            book[force_user] = force_side
        if force_user not in book:
            book[force_user] = force_side
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for c_name, c_side in book.items():
    all_sides.setdefault(c_side, []).append(c_name)

sorted_all_sides = dict(sorted(all_sides.items(), key=lambda x: (-len(x[1]), x[0])))

for current_side, list_of_names in sorted_all_sides.items():
    print(f"Side: {current_side}, Members: {len(list_of_names)}")
    print("\n".join(f"! {name}" for name in sorted(list_of_names)))
