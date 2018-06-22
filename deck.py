from card import Card
from mongo import Mongo
import random

class Deck():

    def __init__(self):
        self.deck = Mongo()
        suits = ('diamonds', 'clubs', 'hearts', 'spades')
        ranks = {v:v for v in range(2,11)}
        ranks["jack"] = 10
        ranks["lady"] = 10
        ranks["king"] = 10
        ranks["ase"] = None
        for suit in suits:
            for k,v in ranks.items():
                self.deck.insertToCollection({suit:{k:v}})


    def __str__(self):
        return "{}".format(len(self.deck))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

d = Deck()
print(d.deck.getCollection())
#d = Deck()
#d.shuffle()
#print([[y for y in x.rank.values()] for x in d.deck])
