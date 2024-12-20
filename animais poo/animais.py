class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_som(self):
        print(f"{self.nome} faz um som desconhecido.")
    
    def alimentar(self):
        print(f'{self.nome} está se alimentando.')
    
    def dormir(self):
        print(f'{self.nome} está dormindo.')


