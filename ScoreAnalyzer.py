class ScoreAnalyzer:

    test = 1

    def maxScore(self, deck):
        score = 0
        for listOfCards in deck.cards:
            for card in listOfCards:
                #print "Card:", card
                CMC = card.convertedManacost()
                #print "Converted Mana Cost:", CMC
                weight = self.weightForCMC(CMC)
                score += weight
                print "CMC:", CMC
                print "Weight:", weight
                print "Score:", score
        return score

    def weightForCMC(self, CMC):
        return {
             1 : 1,
             2 : .9,
             3 : .8,
             4 : .7,
             5 : .6,
             6 : .5,
             7 : .4
        }.get(CMC, 0)
