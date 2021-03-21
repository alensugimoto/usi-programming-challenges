max_shuffles = int(input())
num_cards = 2 ** max_shuffles
cards = input().split()
num_shuffles = 0
while num_shuffles < max_shuffles:
    num_cards_per_pile = 2 ** num_shuffles
    new_cards = []
    for i in range(0, num_cards, 2 * num_cards_per_pile):
        for j in range(num_cards_per_pile - 1, -1, -1):
            new_cards.append(cards[i + j + num_cards_per_pile])
            new_cards.append(cards[i + j])
    cards = new_cards
    num_shuffles += 1
print(" ".join(cards))
