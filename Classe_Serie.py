class Serie:

    def __init__(self, nome, ano, genero, numerodetemporadas):
        self.__nome = nome
        self.__ano = ano
        self.__genero = genero
        self.__numerodetemporadas = numerodetemporadas

    def dadosserie(self):
        nome = str(self.__nome).title()
        return print(f'Nome: {nome} - Ano: {self.__ano} - Gênero: {self.__genero} '
                     f'- Número de Temporadas: {self.__numerodetemporadas}')

