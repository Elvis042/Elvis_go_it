from terrestre import Terrestre

class Carro(Terrestre):

    rodas = 4

    def __init__(self, vel=120, pistoes=4):
        self.pistoes = pistoes
        Terrestre.__init__(self, vel=vel)