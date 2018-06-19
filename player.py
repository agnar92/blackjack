from chips import Chips
from hand import Hand
from deck import Deck

class Player():

    def __init__(self, deck):
        self.my_hand = Hand()
        self.my_chips = Chips()
        self.deck = deck

    def __str__(self):
        return  "Hand {1}: {0}".format(
            ["{} of {}".format(x.suit, {k for k,v in x.rank.items()}) for x in self.my_hand.cards],
            self.__class__.__name__)

    def hit(self):
        card = self.deck.deal()
        if "ase" in card.rank:
            card.rank["ase"] = self.my_hand.adjas_of_ase()
        self.my_hand.values += [x for x in card.rank.values()][0]
        self.my_hand.add_card(card)

    def begin(self):
        self.my_hand.add_card(self.deck.deal())
        self.my_hand.add_card(self.deck.deal())
        for ase in self.my_hand.cards:
            if [k for k in ase.rank if k is "ase"]:
                ase.rank["ase"]=self.my_hand.adjas_of_ase()
        self.my_hand.values = sum([sum({v for k,v in x.rank.items()}) for x in self.my_hand.cards])
