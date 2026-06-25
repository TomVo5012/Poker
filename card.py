import random


class Card:
    # Constructor
    def __init__(self):
        self.number = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.suit = ['♠', '♥', '♦', '♣']
    
    # Pick Randomly 5 cards for dealer
    def dealer_combine_card(self):
        dealer_cards_shuffle = []
        for i in range(5):
            random_card = str(self.number[random.randint(0,12)]) + str(self.suit[random.randint(0,3)])
            dealer_cards_shuffle.append(random_card)
        return dealer_cards_shuffle
    
    # Pick Randomly 2 cards for player
    def player_combine_card(self):
        player_cards_shuffle = []
        for i in range(2):
            random_card = str(self.number[random.randint(0,12)]) + str(self.suit[random.randint(0,3)])
            player_cards_shuffle.append(random_card)
        return player_cards_shuffle