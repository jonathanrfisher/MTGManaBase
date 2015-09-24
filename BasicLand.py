from ColorsOfMana import c

# Represents a basic land.  Can be intialized as being a
# producers of any of the 5 colors in magic.

# The five basic [colors (abrv) - types] are:
# 1. Green (G) - Forst
# 2. White (W) - Plains
# 3. Blue  (U) - Island
# 4. Black (B) - Swamp
# 5. Red   (R) - Mountain

# There is no limit to how many of these can be in a deck.

# Basic lands enter the battlefield untapped.

# Basic lands can be 'fetched' by fetch-lands

class BasicLand:

    def __init__(self, color):
        self.landType = self.getTypeForColor(color)

    def getTypeForColor(self, color):
        return {
             c.W : "Plains",
             c.G : "Forest",
             c.R : "Mountain",
             c.B : "Swamp",
             c.U : "Island"
        }.get(color, "UNKNOWN_COLOR")
