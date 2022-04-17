from collections import deque

vowels = deque(input().split())
consonants = input().split()

rose = list("rose")
tulip = list("tulip")
lotus = list("lotus")
daffodil = list("daffodil")
word_found = ""
win_game = False

while vowels and consonants:

    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    while current_vowel in rose:
        rose.remove(current_vowel)
    while current_consonant in rose:
        rose.remove(current_consonant)
    if len(rose) == 0:
        word_found = "rose"
        win_game = True
        break

    while current_vowel in tulip:
        tulip.remove(current_vowel)
    while current_consonant in tulip:
        tulip.remove(current_consonant)
    if len(tulip) == 0:
        word_found = "tulip"
        win_game = True
        break

    while current_vowel in lotus:
        lotus.remove(current_vowel)
    while current_consonant in lotus:
        lotus.remove(current_consonant)
    if len(lotus) == 0:
        word_found = "lotus"
        win_game = True
        break

    while current_vowel in daffodil:
        daffodil.remove(current_vowel)
    while current_consonant in daffodil:
        daffodil.remove(current_consonant)
    if len(daffodil) == 0:
        word_found = "daffodil"
        win_game = True
        break


if win_game:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
