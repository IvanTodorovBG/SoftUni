deck = input().split(" ")
n = int(input())


for current_shuffle in range(n):
    new_deck = []

    middle_deck = int(len(deck) / 2)
    left_deck = deck[:middle_deck]
    right_deck = deck[middle_deck:]

    for index in range(int(len(deck) / 2)):
        new_deck.append(left_deck[index])
        new_deck.append(right_deck[index])

    deck = new_deck

print(deck)
