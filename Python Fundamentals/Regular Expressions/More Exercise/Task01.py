import re

racers = input().split(", ")
my_dict = {}
data = input()
string_pattern = r"[a-zA-Z]"
num_pattern = r"[0-9]"

while data != "end of race":

    name = "".join(re.findall(string_pattern, data))
    if name in racers:
        numbers = re.findall(num_pattern, data)
        nums = sum([int(x) for x in numbers])
        if name not in my_dict:
            my_dict[name] = 0
        my_dict[name] += nums

    data = input()

sorted_my_dict = dict(sorted(my_dict.items(), key=lambda kvr: -kvr[1]))

answer = list(sorted_my_dict.keys())

print(f"1st place: {answer[0]}")
print(f"2nd place: {answer[1]}")
print(f"3rd place: {answer[2]}")
