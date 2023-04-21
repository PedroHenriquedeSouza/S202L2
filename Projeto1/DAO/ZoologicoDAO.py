from database.Database import Database
from model.Animal import Animal
import json

class ZoologicoDAO:
    def __init__(self):
        self.db = Database("Zoologico", "Animais")
        self.data = self.db.collection

    def createAnimal(self, animal: Animal):
        try:
            if (self.data.find_one({"id": animal.id})):
                print(f"Já existe um animal cadastrado com esse id: {animal.id}")
            else:
                result = self.data.insert_one(animal.__dict__)
                animalId = str(result.inserted_id)
                print(f"Animal {animal.nome} created with id: {animalId}")
        except Exception as error:
            print(f"An error occurred while creating animal: {error}")
            return None
        
    def readAnimal(self, animal_id) -> dict:
        try:
            animal = self.data.find_one({"id": animal_id})
            if animal:
                print(f"Animal found: {animal}")
                return animal
            else:
                print(f"No animal found with id {animal_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading animal: {error}")
            return None

    def updateAnimal(self, animal: Animal) -> int:
        try:
            result = self.data.update_one({"id": animal.id}, {"$set": {"nome": animal.nome, "especie": animal.especie, "idade": animal.idade}})
            if result.modified_count:
                print(f"Animal {animal.id} updated with name {animal.nome}, specie {animal.especie}, age {animal.idade}")
            else:
                print(f"No animal found with id {animal.id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")
            return None

    def deleteAnimal(self, animalId: str) -> int:
        try:
            result = self.data.delete_one({"id": animalId})
            if result.deleted_count:
                print(f"Animal {animalId} deleted")
            else:
                print(f"No animal found with id {animalId}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting animal: {error}")
            return None