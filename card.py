
class Card():
    """
    Card class

    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{0} of {1}".format(self.suit, self.rank)

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit
