text = input().split(" ")

new_text = []

for current_word in text:
    word = list(current_word)
    digits = []
    no_digits = []
    new_word = []

    for letters in word:
        if letters.isdigit():
            digits.append(letters)
        if letters.isalpha():
            no_digits.append(letters)

    first_alpha = chr(int("".join([str(i) for i in digits])))
    new_word.append(first_alpha)
    new_word += no_digits

    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    new_word = "".join(new_word)
    new_text.append(new_word)

print(" ".join(new_text))