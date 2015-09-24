from ColorsOfMana import c
from BasicLand import BasicLand
#from ManaBase import ManaBase

class ManaBaseIterator:

    def __init__(self, colors):
        self.colors = colors
        self.currentManaBase = self.startingManaBaseWithColors(colors)

    #Currently only works for monocolored decks!
    def startingManaBaseWithColors(self, colors):
        lands = []
        if len(colors) == 1:
            basicLand = self.basicLandForColor(colors[0])
            lands = [basicLand for i in range(24)]
        return lands

    #Currently does nothing!
    def nextManaBase(self):
        return self.startingManaBaseWithColors()

    def basicLandForColor(self, color):
        return {
             c.W : BasicLand(c.W),
             c.G : BasicLand(c.G),
             c.R : BasicLand(c.R),
             c.B : BasicLand(c.B),
             c.U : BasicLand(c.U),
        }.get(color, BasicLand(69))
