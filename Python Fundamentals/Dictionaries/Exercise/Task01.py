string = input().split(" ")
new_string = "".join(string)
new_dict = {}
for letter in new_string:
    new_dict[letter] = new_string.count(letter)

for key, value in new_dict.items():
    print(f"{key} -> {value}")