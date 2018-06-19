class Hand():

    def __init__(self):
        self.cards = []
        self.values = 0

    def add_card(self, card):
        return self.cards.append(card)

    def adjas_of_ase(self):
        return (1 if self.values >= 10 else 11)
