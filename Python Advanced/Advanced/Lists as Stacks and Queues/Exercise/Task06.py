string = input()
open_brackets = []

balanced = True
for el in string:
    if el in '{[(':
        open_brackets.append(el)
    elif el in '}])':
        if not open_brackets:
            balanced = False
            break

        if el == "}":
            if open_brackets.pop() == "{":
                continue
            else:
                balanced = False
                break
        elif el == "]":
            if open_brackets.pop() == "[":
                continue
            else:
                balanced = False
                break
        elif el == ")":
            if open_brackets.pop() == "(":
                continue
            else:
                balanced = False
                break

if balanced and len(open_brackets) == 0:
    print("YES")
else:
    print("NO")