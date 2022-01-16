command = input()

notes = []

for x in range(11):
    notes.append(0)

while command != "End":

    command = command.split("-")

    importance = int(command[0])
    note = command[1]

    notes.pop(importance)
    notes.insert(importance, note)

    command = input()

answer = [i for i in notes if i != 0]
print(answer)
