import random

class Coin:
    value, flipCtr, headsCtr, tailsCtr, bias = 0,0,0,0,0
    upFace, name = "",""
    coins = {
        "penny" : 0.01,
        "nickel" : 0.05,
        "dime" : 0.10,
        "quarter" : 0.25,
        "dollar" : 1.00
    }

    def __init__(self):
        self.upFace = "heads"
        self.bias = 0.5

    def __init__(self, s):
        self.name = s
        self.assignValue(self.name)
        self.upFace = "heads"
        self.bias = 0.5

    def __init__(self, s, nowFace):
        self.name = s
        self.assignValue(self.name)
        self.upFace = nowFace
        self.bias = 0.5

    def assignValue(self, s):
        self.value = self.coins.get(s)
        return self.value
    
    def flip(self):
        a = random.random()
        if (a > self.bias):
            self.upFace = "tails"
            self.tailsCtr += 1
        else:
            self.upFace = "heads"
            self.headsCtr += 1
        return self.upFace

    def reset(self, s, d):
        self.upFace = s
        self.bias = d

    def equals(self, other):
        return self.upFace == other.upFace
    
    def __str__(self):
        return self.name + " " + self.upFace