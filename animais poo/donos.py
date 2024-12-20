class Dono:
    def __init__(self, nome):
        self.nome = nome

    def chamar_animal(self, animal):
        print(f'{self.nome} está chamando o(a) {animal.nome}.')

