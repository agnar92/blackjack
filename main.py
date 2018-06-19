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
    dd = Dealer(d)

    player_1.begin()
    dd.begin()

    print(player_1)
    print(dd)

    return d, player_1, dd


def main():
    deck, player, dealer = start()
    print("Bet: {1} and {0}".format(player.my_chips, player.my_chips.bet))
    while player.my_chips.total is not 0:
        dealer.take_bet(player=player, bet=int(input('How much you will bet? \n')))
        while True:
            out = input("Hit or Stand \n").lower()
            if out == "hit":
                player.hit()
                if player.my_hand.values > 21:
                    print("Player lose!")
                    player.my_chips.lose_bet()
                    break
                elif player.my_hand.values == 21:
                    print("Player Win!")
                    player.my_chips.win_bet()
                    break

            else:
                dealer.show_2nd_card()
                print(player)
                print(dealer)
                while dealer.my_hand.values < 17:
                    dealer.hit()
                    print("Dealer value: %s" % dealer.my_hand.values)
                if player.my_hand.values > dealer.my_hand.values or player.my_hand.values == 21:
                    print("Player Win!")
                    player.my_chips.win_bet()
                    break
                else:
                    print("Player lose!")
                    player.my_chips.lose_bet()
                    break

            print(player)
            print(dealer)
            print("Bet: {1} and {0}".format(player.my_chips, player.my_chips.bet))
            print("PLayer value: %s " % player.my_hand.values)

        #reset
        deck, player, dealer = start()

if __name__ == '__main__':
    main()
