class Filme:

    def __init__(self, nome, ano, genero, duracao):
        self.__nome = nome
        self.__ano = ano
        self.__genero = genero
        self.__duracao = duracao

    def dadosfilme(self):
        nome = str(self.__nome).title()
        return print(f'Nome: {nome} - Ano: {self.__ano} - Gênero: {self.__genero} - Duração: {self.__duracao}')

