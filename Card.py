from ColorsOfMana import c

class Card:

    # colorless should be an integer representing total colorless
    # cost.
    # colors should be an array of individual colors in the cost.
    def __init__(self, colorless, colors):
        self.colorless = colorless
        self.colors = colors

    def convertedManacost(self):
        #print "CALCULATED CONVERTED MANA COST"
        totalColorlessMana = self.colorless
        totalColoredMana = len(self.colors)
        #print "colorless:",totalColorlessMana, "Colored:", totalColoredMana
        return totalColorlessMana + totalColoredMana

    def whiteMana(self):
        return self.coloredManaCountHelper(c.W)

    def coloredManaCountHelper(self, colorToCount):
        totalColored = 0

        for x in self.colors:
            if x == colorToCount:
                totalColored += 1

        return totalColored
