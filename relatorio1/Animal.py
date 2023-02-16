class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.som)
            
    def mudar_cor(self, nova_cor):
        self.cor = nova_cor
        print("A cor do animal: " + self.nome + "foi alterada para: " + nova_cor)
        return