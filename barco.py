from aquatico import Aquatico

class Barco(Aquatico):
    def __init__(self, vel=6, helices=1):
        self.helices = helices
        Aquatico.__init__(self, vel=vel)