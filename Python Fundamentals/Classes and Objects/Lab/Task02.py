class Party:
    def __init__(self):
        self.people = []


going_people = Party()

command = input()

while command != "End":
    going_people.people.append(command)
    command = input()

print(f"Going: {', '.join(going_people.people)}")
print(f"Total: {len(going_people.people)}")