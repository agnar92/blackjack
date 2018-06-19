from deck import Deck
from player import Player
from dealer import Dealer
from chips import Chips

def start():
    # Genarate Deck
    d = Deck()
    d.shuffle()

    # give card for player and dealer
    player_1 = Player(d)
    dealer = Dealer(d)

    player_1.begin()
    dealer.begin()

    print(player_1)
    print(dealer)

    return d, player_1, dealer


def main():
    deck, player, dealer = start()
    print("Bet: {1} and {0}".format(player.my_chips, player.my_chips.bet))
    while player.my_chips.total is not 0:
        dealer.take_bet(player=player, bet=int(input('How much you will bet? \n')))
        while player.my_hand.values < 20 or dealer.my_hand.values < 17:
            out = input("Hit or Stand \n").lower()
            if out == "hit":
                player.hit()
            else:
                dealer.hit()
            print(player)
            print(dealer)
            print("Bet: {1} and {0}".format(player.my_chips, player.my_chips.bet))
            print(player.my_hand.values)

    # TODO: check value and if is a ase give a correct values
    # TODO: loop for playing, starts hit and stand
    # TODO: Bank?
    # TODO: When wan? or lose?



if __name__ == '__main__':
    main()
