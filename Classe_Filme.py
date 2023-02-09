from Classe_Programa import Programa
class Filme(Programa):

    def __init__(self, nome, ano, genero, duracao):
        super().__init__(nome,ano,genero)
        self.__duracao = duracao



    def dadosfilme(self):
        #nome = str(self.__nome).title()
        return print(f'Nome: {self.__nome} - Ano: {self.__ano} - Gênero: {self.__genero} - Duração: {self.__duracao} '
                     f'- Likes: {self.__likes}')

