class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def __str__(self):
        return "Total: {}".format(self.total)

    def win_bet(self):
        self.total += self.bet*2
        self.bet = 0

    def lose_bet(self):
        self.bet = 0
