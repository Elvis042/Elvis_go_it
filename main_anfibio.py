from anfibio import Anfibio

novo_anfibio = Anfibio()

for atr in dir(novo_anfibio):

    if not atr.startswith('__'):

        print(atr, '=', getattr(novo_anfibio, atr))
