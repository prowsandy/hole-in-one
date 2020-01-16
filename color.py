class Color:
    def __init__(self,color_name,multipliervalue,is_bokya):
        self.color_name = color_name
        self.multipliervalue = multipliervalue
        self.is_bokya = is_bokya

    def __str__(self):
        return self.color_name

    def getMultiplier(self):
        return self.multipliervalue

    def getIsBokya(self):
        return self.is_bokya
