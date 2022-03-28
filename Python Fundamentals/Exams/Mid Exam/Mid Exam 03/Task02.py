targets = [int(x) for x in input().split(" ")]
command = input()

count = 0

while command != "End":

    index = int(command)

    if 0 <= index < len(targets) and targets[index] != -1:
        current_target = targets[index]
        targets[index] = -1
        count += 1

        for idx, number in enumerate(targets):
            if number > current_target:
                targets[idx] -= current_target
            elif 0 < number <= current_target:
                targets[idx] += current_target

        # targets_comprehension = [targets[idx] - current_target if number > current_target else targets[idx] + current_target if 0 < number <= current_target for idx, number in enumerate(targets)]

    command = input()

final_targets = " ".join([str(i) for i in targets])

print(f"Shot targets: {count} -> {final_targets}")
