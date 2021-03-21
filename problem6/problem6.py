numbers = input().split()
max_shuffles = int(numbers[0])
positions = []
for _ in range(int(numbers[1])):
    pos = int(input()) - 1
    num_shuffles = 0
    while num_shuffles < max_shuffles:
        num_cards_per_pile = 2 ** num_shuffles
        # position relative to a pair of piles
        pair_pos = pos % (2 * num_cards_per_pile)
        # position relative to a pile
        pile_pos = pair_pos % num_cards_per_pile
        # new position
        pos += 2 * (num_cards_per_pile - pile_pos) - pair_pos - 1
        if pair_pos >= num_cards_per_pile:
            pos -= 1
        # prepare for next iteration
        num_shuffles += 1
    positions.append(pos + 1)
for pos in positions:
    print(pos)
