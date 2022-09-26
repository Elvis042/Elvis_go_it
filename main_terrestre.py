from carro import Carro

novo_carro = Carro()

for atr in dir(novo_carro):

    if not atr.startswith('__'):

        print(atr, '=', getattr(novo_carro, atr))
