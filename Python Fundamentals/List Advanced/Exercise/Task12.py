command = input()
all_language = {}
submissions = {}
max_points = {}
while command != "exam finished":

    command = command.split("-")

    # check for no banned
    if len(command) == 3:
        language = command[1]
        username = command[0]
        points = int(command[2])

        # collect all submissions
        submissions.setdefault(language, []).append(username)

        # collect data
        if language not in all_language:
            all_language[language] = {}
            all_language[language][username] = points

        # add new name + points in existing language
        if language in all_language and username not in all_language[language]:
            all_language[language][username] = points

        # separate only high scores
        if points > all_language[language][username]:
            all_language[language][username] = points

    # check for banned
    elif len(command) == 2:
        username = command[0]
        banned = command[1]

        # remove banned
        for key in all_language.keys():
            if username in all_language[key]:
                del all_language[key][username]


    command = input()

# result with name + max points without language
for name_p in all_language.values():
    for current_name, current_points in name_p.items():
        max_points[current_name] = current_points

sorted_max_points = dict(sorted(max_points.items(), key=lambda x: (-x[1], x[0])))

print("Results:")
print("\n".join(f"{k} | {v}" for k, v in sorted_max_points.items()))
print("Submissions:")
print("\n".join(f"{lang} - {len(attempts)}" for lang, attempts in sorted(submissions.items())))




