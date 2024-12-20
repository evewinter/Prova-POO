from animais import Animal

class TiposAnimais:
    class Gato(Animal):
        def __init__(self, nome, idade):
            super().__init__(nome, idade)
        
        def fazer_som(self):
            print(f'{self.nome} está miando: Miau Miau!')

        def arranhar(self):
            print(f'{self.nome} está arranhando.')

    class Cao(Animal):
        def __init__(self, nome, idade):
            super().__init__(nome, idade)
        
        def fazer_som(self):
            print(f'{self.nome} está latindo: Au Au!')
        
        def caçar(self):
            print(f'{self.nome} está caçando.')

    class Passaro(Animal):
        def __init__(self, nome, idade):
            super().__init__(nome, idade)
        
        def fazer_som(self):
            print(f'{self.nome} está cantando: Piui Piui!')
        
        def voar(self):
            print(f'{self.nome} está voando.')
