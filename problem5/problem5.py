max_shuffles = int(input())
cards = input().split()
num_shuffles = 0
while num_shuffles < max_shuffles:
    num_cards_per_pile = 2 ** num_shuffles
    while num_cards_per_pile > 1:
        cards = cards[num_cards_per_pile // 2:num_cards_per_pile] + cards[3 * num_cards_per_pile // 2:] + cards[:num_cards_per_pile // 2] + cards[num_cards_per_pile:3 * num_cards_per_pile // 2]
        num_cards_per_pile //= 2
    cards[::2], cards[1::2] = cards[1::2], cards[::2]
    num_shuffles += 1
print(" ".join(cards))
