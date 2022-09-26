class Cadastro:
    __nome: str
    __idade: int
    sexo: str
    rg: int
    cpf: int

    def __init__(self, sexo, rg, cpf, nome=None, idade=0):
        self.__nome = nome
        self.__idade = idade
        self.sexo = sexo
        self.rg = rg
        self.cpf = cpf
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    