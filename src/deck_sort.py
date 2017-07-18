from insertion_sort import insertion_sort
"""This will sort a deck of cards"""
"""['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']"""
"""['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']"""


def deck_sort(deck):
    """This will sort a random deck of cards"""
    sorted_deck = []
    letters = ['A', 'T', 'J', 'Q', 'K']
    while len(sorted_deck) < len(deck):
        idx = 0
        for card in deck:
            if card in letters:
                
            else:
                try:
                    if sorted_deck[idx] >= card:
                        sorted_deck.insert(idx, card)
                        idx = 0
                        break
                    else:
                        idx += 1
                except IndexError:
                    sorted_deck.append(card)
                    idx = 0
                    break
    return sorted_deck
