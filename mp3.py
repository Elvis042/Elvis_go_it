from pendrive import Pendrive

class Mp3(Pendrive):
    def __init__(self, tamanho, interface='2.0', turner=False):
        self.turner = turner
        Pendrive.__init__(self,tamanho, interface)

