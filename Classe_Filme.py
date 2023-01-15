class Filme:

    def __init__(self, nome, ano, genero, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.__genero = genero
        self.__duracao = duracao
        self.__likes = 0

    def darlike(self):
        self.__likes += 1

    def dadosfilme(self):
        #nome = str(self.__nome).title()
        return print(f'Nome: {self.__nome} - Ano: {self.__ano} - Gênero: {self.__genero} - Duração: {self.__duracao} '
                     f'- Likes: {self.__likes}')

