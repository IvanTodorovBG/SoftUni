text = input()
word = ""
count_C = False
count_O = False
count_N = False

while text != "End":
    if 65 <= ord(text) <= 90 or 97 <= ord(text) <= 122:
        if text == "c" and count_C:
            word += text
        elif text == "o" and count_O:
            word += text
        elif text == "n" and count_N:
            word += text
        if text == "c":
            count_C = True
        elif text == "n":
            count_N = True
        elif text == "o":
            count_O = True
        else:
            word += text
        if count_C and count_N and count_O:
            print(word, end=" ")
            word = ""
            count_C = False
            count_N = False
            count_O = False
    text = input()
