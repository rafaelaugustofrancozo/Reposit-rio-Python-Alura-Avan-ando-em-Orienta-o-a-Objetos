class Serie:

    def __init__(self, nome, ano, genero, numerodetemporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.__genero = genero
        self.__numerodetemporadas = numerodetemporadas
        self.__likes = 0

    def darlike(self):
        self.__likes += 1

    def dadosserie(self):
        #nome = str(self.__nome).title()
        return print(f'Nome: {self.__nome} - Ano: {self.__ano} - Gênero: {self.__genero} '
                     f'- Número de Temporadas: {self.__numerodetemporadas} - Likes: {self.__likes}')

