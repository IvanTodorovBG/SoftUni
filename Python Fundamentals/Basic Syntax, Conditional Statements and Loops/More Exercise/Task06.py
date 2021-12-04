command = input()

coffee_counter = 0
events_lower = ["coding", "dog", "cat", "movie"]
events_upper = [x.upper() for x in events_lower]

while command != "END":
    if command in events_lower:
        coffee_counter += 1
    if command in events_upper:
        coffee_counter += 2

    command = input()

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)
