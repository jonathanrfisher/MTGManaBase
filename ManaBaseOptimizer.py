from Deck import Deck
from Card import Card
from ColorsOfMana import c
from DeckGenerator import DeckGenerator
from ManaBaseIterator import ManaBaseIterator
from ScoreAnalyzer import ScoreAnalyzer

class ManaBaseOptimizer:

    deckGen = DeckGenerator()

    whiteWeenie = deckGen.whiteWeenie()
    scoreAnalyzer = ScoreAnalyzer()

    print "Max Score for whiteWeenie:", scoreAnalyzer.maxScore(whiteWeenie)

    # Given our white weenie deck, find the optimal mana configuration.
    # (Obviously all plains)

    cards = whiteWeenie.cards

    manaBaseIter = ManaBaseIterator([c.W]);

    #print "ManaBase:", manaBaseIter.currentManaBase

    #for land in manaBaseIter.currentManaBase:
        #print land.landType

    #for arrayOfCards in cards:
        # Each member of cards will be an array of cards
        #for card in arrayOfCards:
            #print "CMC:", card.convertedManacost()
            #print card
