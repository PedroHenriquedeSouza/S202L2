from Animal import Animal

class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho
    def trombar():
        print("uuuuh!")
    def mudar_tamanho(self, tamanho):
        self.tamanho = tamanho

