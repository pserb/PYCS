class BigSib:
    helloMsg = ""

    def __init__(self):
        pass

    def setHelloMsg(self, helloMsg):
        self.helloMsg = helloMsg

    def greet(self, name):
        return self.helloMsg + " " + name
