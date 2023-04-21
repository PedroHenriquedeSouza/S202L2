from model.Habitat import Habitat

class Animal:
    def __init__(self, id, nome, especie, idade, habitat: Habitat):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat.__dict__

    def __init__(self, id, nome, especie, idade):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.idade = idade