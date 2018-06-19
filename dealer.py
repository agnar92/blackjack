from chips import Chips
from hand import Hand
from player import Player

class Dealer(Player):

    def __init__(self, deck):
        self.my_hand = Hand()
        self.deck = deck
        self.i = 1

    def __str__(self):
        return  "Hand {1}: {0}".format(
            ["{} of {}".format(
                self.my_hand.cards[x].suit,
                {k for k, v in self.my_hand.cards[x].rank.items()}) for x in range(0,self.i)],
            self.__class__.__name__)

    def hit(self):
        card = self.deck.deal()
        print(card)
        self.i += 1
        if "ase" in card.rank:
            card.rank["ase"] = self.my_hand.adjas_of_ase()
        self.my_hand.values += [x for x in card.rank.values()][0]
        self.my_hand.add_card(card)

    def show_2nd_card(self):
        self.i += 1

    def take_bet(self, player, bet):
        player.my_chips.total -= bet
        player.my_chips.bet += bet
