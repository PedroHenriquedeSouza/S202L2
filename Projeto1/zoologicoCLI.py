from DAO.ZoologicoDAO import ZoologicoDAO
from model.Animal import Animal
from model.Cuidador import Cuidador
from model.Habitat import Habitat

class ZoologicoCLI:
    def __init__(self):
        self.zoologico = ZoologicoDAO()

    def menu(self):
        print("Selecione uma opção:")
        print("1 - Adicionar um animal")
        print("2 - Procurar um animal")
        print("3 - Atualizar um animal")
        print("4 - Deletar um animal")

    def createAnimal(self):
        print("Entre com as seguintes informações: ")
        print()

        idAnimal = input("ID do animal: ")
        nomeAnimal = input("Nome do animal: ")
        especieAnimal = input("Espécie: ")
        idadeAnimal = input("Idade: ")
        idHabitat = input("ID do habitat: ")
        nomeHabitat = input("Nome do habitat: ")
        tipoAmbiente = input("Tipo do ambiente: ")
        idCuidador = input("ID do cuidador: ")
        nomeCuidador = input("Nome do cuidador: ")
        documentoCuidador = input("Documento do cuidador: ")

        cuidador = Cuidador(id=idCuidador , nome=nomeCuidador, documento=documentoCuidador)
        habitat = Habitat(id=idHabitat, nome=nomeHabitat, tipoAmbiente=tipoAmbiente, cuidador=cuidador)
        animal = Animal(id=idAnimal, nome=nomeAnimal, especie=especieAnimal, idade=idadeAnimal, habitat=habitat)

        self.zoologico.createAnimal(animal=animal)

    def readAnimal(self):
        animalID = input(print("Entre com o ID do animal desejado: "))
        self.zoologico.readAnimal(animal_id=animalID)
    def updateAnimal():
        pass
    def deleteAnimal():
        pass