from Deck import Deck
from Card import Card
from ColorsOfMana import c


# The purpose of this class will be to generate sets of
# Decks for the purpose of testing them against as candidate
# manabases

# I'm not sure if this class will actually perform any of the
# testing or recording.  Ideally it would NOT and would simply
# have the job of generating decks.

class DeckGenerator:

    # We want 36 cards representing a typical white weenie deck
    def whiteWeenie(self):
        oneCC = Card(0,[c.W])
        twoCC = Card(0,[c.W,c.W])
        twocC = Card(1,[c.W])
        threecCC = Card(1,[c.W,c.W])
        threeccC = Card(2,[c.W])
        # 36 Cards, a mix of the above costs.
        cards = [[oneCC,oneCC,oneCC,oneCC,oneCC,oneCC,oneCC,
        oneCC,oneCC,oneCC,oneCC,oneCC],[twoCC,twoCC,twoCC,
        twoCC,twoCC,twoCC,twoCC,twoCC,twoCC,twoCC,twoCC,twoCC,
        twocC,twocC,twocC,twocC],[threecCC,threecCC,threecCC,
        threecCC,threecCC,threeccC,threeccC,threeccC]]

        return Deck(cards)
