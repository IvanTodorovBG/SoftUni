all_contests = {}
collection_total_points = {}

info = input()
while info != "no more time":
    info = info.split(" -> ")
    username = info[0]
    contest = info[1]
    points = int(info[2])

    # collect info
    if contest not in all_contests:
        all_contests[contest] = {}
        all_contests[contest][username] = points
    else:
        if username not in all_contests[contest]:
            all_contests[contest][username] = points
        else:
            if points > all_contests[contest][username]:
                all_contests[contest][username] = points

    info = input()

# collect info for total points
for _ in all_contests.values():
    for name, current_points in _.items():
        if name not in collection_total_points:
            collection_total_points[name] = 0
        collection_total_points[name] += current_points

# sort total points
sorted_total_points = dict(sorted(collection_total_points.items(),key=lambda kvp: (-kvp[1], kvp[0])))

for current_contest in all_contests:
    print(f"{current_contest}: {len(all_contests[current_contest])} participants")
    sorted_d = dict(sorted(all_contests[current_contest].items(),key=lambda kvp: (-kvp[1], kvp[0])))
    count = 1
    for k, v in sorted_d.items():
        print(f'{count}. {k} <::> {v}')
        count += 1


print("Individual standings:")
count = 1
for k, v in sorted_total_points.items():
    print(f'{count}. {k} -> {v}')
    count += 1