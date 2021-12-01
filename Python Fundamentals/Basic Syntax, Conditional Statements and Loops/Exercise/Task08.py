string = input()
string2 = input()

previously_string = ""
new_string = ""

for i in range(1, len(string) + 1):
    new_string = string2[:i] + string[i:]

    if new_string != string and new_string != previously_string:
        print(new_string)

    previously_string = new_string
    