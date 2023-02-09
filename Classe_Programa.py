class Programa:

    def __init__(self, nome, ano, genero):
        self.__nome = nome
        self.__ano = ano
        self.__genero = genero
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def darlike(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def ano(self):
        return self.__ano

    @property
    def genero(self):
        return self.__genero