from database.Database import Database
from bson.objectid import ObjectId
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

    def update_book(self, book_id: str, title: str, author: str, year: int, price: float) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(book_id)}, {"$set": {"titulo": title, "autor": author, "year": year, "preco": price}})
            if result.modified_count:
                print(f"Book {book_id} updated with title {title}, author {author}, year {year} and price {price}")
            else:
                print(f"No book found with id {book_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating book: {error}")
            return None
        
    def update_book_price(self, book_id: str, price: float) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(book_id)}, {"$set": {"preco": price}})
            if result.modified_count:
                print(f"Book {book_id} updated with price {price}")
            else:
                print(f"No book found with id {book_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating book: {error}")
            return None

    def delete_book(self, book_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(book_id)})
            if result.deleted_count:
                print(f"Book {book_id} deleted")
            else:
                print(f"No book found with id {book_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting book: {error}")
            return None