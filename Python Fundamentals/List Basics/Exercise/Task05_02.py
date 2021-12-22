deck = input().split(" ")
shuffles = int(input())


for current_shuffle in range(shuffles):
    mid_deck = int(len(deck) // 2)
    left_deck = deck[:mid_deck]
    right_deck = deck[mid_deck:]
    new_deck = []
    for current_deck in range(mid_deck):

        new_deck.append(left_deck[current_deck])
        new_deck.append(right_deck[current_deck])
    deck = new_deck

print(deck)
