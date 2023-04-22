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

        idAnimal = int(input("ID do animal: "))
        nomeAnimal = input("Nome do animal: ")
        especieAnimal = input("Espécie: ")
        idadeAnimal = int(input("Idade: "))
        idHabitat = int(input("ID do habitat: "))
        nomeHabitat = input("Nome do habitat: ")
        tipoAmbiente = input("Tipo do ambiente: ")
        idCuidador = int(input("ID do cuidador: "))
        nomeCuidador = input("Nome do cuidador: ")
        documentoCuidador = int(input("Documento do cuidador: "))

        cuidador = Cuidador(id=idCuidador , nome=nomeCuidador, documento=documentoCuidador)
        habitat = Habitat(id=idHabitat, nome=nomeHabitat, tipoAmbiente=tipoAmbiente, cuidador=cuidador)
        animal = Animal(id=idAnimal, nome=nomeAnimal, especie=especieAnimal, idade=idadeAnimal, habitat=habitat)

        self.zoologico.createAnimal(animal=animal)

    def readAnimal(self):
        animalID = input("Entre com o ID do animal desejado: ")
        self.zoologico.readAnimal(animal_id=animalID)
    def updateAnimal(self):
        animalID = input("Entre com o ID do animal que deseja atualizar: ")
        animalDict = self.zoologico.readAnimal(animal_id=animalID)
        
        if animalDict:
            nome = input("Nome do animal: ")
            especie = input("Espécie: ")
            idade = input("Idade: ")
            animal = Animal(id=animalDict["id"], idade=idade, especie=especie, nome=nome, habitat=animalDict["habitat"])
            self.zoologico.updateAnimal(animal=animal)
        else:
            print("Animal não localizado!")
    def deleteAnimal(self):
        animalID = input("Entre com o ID do animal que deseja deletar: ")
        if self.zoologico.readAnimal(animal_id=animalID):
            self.zoologico.deleteAnimal(animalID)
        else:
            print("Animal não localizado!")