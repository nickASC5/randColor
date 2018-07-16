from random import random, choice

def randInt(bound): # returns random int from 0 to bound
    return int(random() * bound)

class RGB():
    def __init__(self,minimum,maximum):
        self.min = min([minimum,maximum])
        self.max = max([minimum,maximum])
        self.delta = self.max - self.min 

    def genColor(self):
        return randInt(self.delta) + self.min

class Palette():
    def __init__(self,r,g,b,a=RGB(255,255)):

        self.rgb = [r,g,b]
    
    def genColor(self):
        return tuple(i.genColor() for i in self.rgb)

class MultiPalette():
    def __init__(self,*palettes):
        self.palettes = palettes

    def genColor(self):
        return choice(self.palettes).genColor()

RED = Palette(RGB(200,235),RGB(50,51),RGB(50,51))
GREEN = Palette(RGB(50,51),RGB(200,235),RGB(50,51))
BLUE = Palette(RGB(50,51),RGB(50,51),RGB(200,235))
BRIGHT = MultiPalette(RED,GREEN,BLUE)


DARK_RED = Palette(RGB(50,150),RGB(0,10),RGB(0,10))