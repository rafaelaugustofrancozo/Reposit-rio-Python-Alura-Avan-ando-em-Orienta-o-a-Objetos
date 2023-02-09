from Classe_Programa import Programa
class Serie(Programa):

    def __init__(self, nome, ano, genero, numerodetemporadas):
        super().__init__(nome, ano, genero)
        self.__numerodetemporadas = numerodetemporadas


    def dadosserie(self):
        #nome = str(self.__nome).title()
        return print(f'Nome: {self.nome} - Ano: {self.ano} - Gênero: {self.genero} '
                     f'- Número de Temporadas: {self.__numerodetemporadas} - Likes: {self.likes}')

