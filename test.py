import random, statistics

def step_count(k):
    step_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 5, 5]
    i = k % 13
    return step_list[i]

def shuffle_deck(card_num):
    deck = []
    cards = list(range(card_num))

    for k in range(card_num):
        i = random.randint(0, len(cards)-1)
        deck.append(cards.pop(i))
    
    return deck

def kruskal(deck, start_pos):
    pos = start_pos
    step = step_count(deck[start_pos])

    while True:
        if pos + step > len(deck) - 1:
            break
        else:
            pos += step
            step = step_count(deck[pos])

    return deck[pos]

def main(card_num):
    deck = shuffle_deck(card_num)
    final_cards = []
    num = 0

    for i in range(10):
        final_cards.append(kruskal(deck, i))

    num = final_cards.count(statistics.mode(final_cards))
    print(final_cards)
    print(num)
    return num/10

j = []
for x in range(100):
    j.append(main(104))

print(statistics.mean(j))