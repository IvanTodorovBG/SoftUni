command = input()
company_users = {}

# add all company users in dictionary
while command != "End":

    command = command.split(" -> ")
    company = command[0]
    users = command[1]

    company_users.setdefault(company, []).append(users)

    command = input()

# remove duplicating users
for k, v in company_users.items():
    new_v = sorted(set(v), key=v.index)
    company_users[k] = new_v

# sort
sorted_company_users = dict(sorted(company_users.items(), key=lambda x: x[0]))

# print
for key, value in sorted_company_users.items():
    print(key)
    print("\n".join(f"-- {val}" for val in sorted_company_users[key]))
