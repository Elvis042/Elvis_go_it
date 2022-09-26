from barco import Barco

novo_barco = Barco()

for atr in dir(novo_barco):

    if not atr.startswith('__'):

        print(atr, '=', getattr(novo_barco, atr))
