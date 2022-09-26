from barco import Barco
from carro import Carro

class Anfibio(Carro, Barco):
    def __init__(self, vel_terra=80, vel_agua=4, pistoes=6, helices=2):

        Carro.__init__(self, vel=vel_terra, pistoes=pistoes)
        Barco.__init__(self, vel=vel_agua, helices=helices)