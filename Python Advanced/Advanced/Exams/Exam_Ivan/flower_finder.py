from collections import deque


def remove_vowel(c_vowel, current_flower):
    while c_vowel in current_flower:
        current_flower.remove(c_vowel)
    return flower


def remove_consonant(c_consonant, current_flower):
    while c_consonant in current_flower:
        current_flower.remove(c_consonant)
    return flower


vowels = deque(input().split())
consonants = input().split()

flowers = ["rose", "tulip", "lotus", "daffodil"]
rose = list("rose")
tulip = list("tulip")
lotus = list("lotus")
daffodil = list("daffodil")
found_word = ''
you_won_game = False

while vowels and consonants:

    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for idx, flower in enumerate([rose, tulip, lotus, daffodil]):
        if current_vowel in flower:
            flower = remove_vowel(current_vowel, flower)
        if current_consonant in flower:
            flower = remove_consonant(current_consonant, flower)

        if len(flower) == 0:
            found_word = flowers[idx]
            you_won_game = True
            break
    if you_won_game:
        break

if you_won_game:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")