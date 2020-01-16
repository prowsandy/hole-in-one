from color import Color
import random

class GameObject:
    colors = []
    gray = Color("Gray",0,True)
    red = Color("Red",17,False)
    yellow = Color("Yellow",7,False)
    green = Color("Green",5,False)
    blue = Color("Blue",3,False)
    pink = Color("Pink",2,False)
    def __init__(self):

        self.colors.append(self.gray)

        self.colors.append(self.red)

        self.colors.append(self.yellow)
        self.colors.append(self.yellow)

        self.colors.append(self.green)
        self.colors.append(self.green)
        self.colors.append(self.green)

        self.colors.append(self.blue)
        self.colors.append(self.blue)
        self.colors.append(self.blue)
        self.colors.append(self.blue)

        self.colors.append(self.pink)
        self.colors.append(self.pink)
        self.colors.append(self.pink)
        self.colors.append(self.pink)
        self.colors.append(self.pink)
        self.colors.append(self.pink)
        self.colors.append(self.pink)

    def getRandomColorResult(self):
        return random.choice(self.colors)

    def getBoardColors(self):
        return self.colors

    def getBoardSize(self):
        return len(self.colors)

    def getReward(self,bet,Color):
        color = Color
        p = bet * color.getMultiplier()
        return p
