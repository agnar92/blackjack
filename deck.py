from card import Card
import random

class Deck():

    def __init__(self):
        self.deck = []
        suits = ('diamonds', 'clubs', 'hearts', 'spades')
        ranks = {v:v for v in range(2,11)}
        ranks["jack"] = 10
        ranks["lady"] = 10
        ranks["king"] = 10
        ranks["ase"] = None
        for suit in suits:
            for k,v in ranks.items():
                self.deck.append(Card(suit, {k:v}))

    def __str__(self):
        return "{}".format(len(self.deck))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


#d = Deck()
#d.shuffle()
#print([[y for y in x.rank.values()] for x in d.deck])
