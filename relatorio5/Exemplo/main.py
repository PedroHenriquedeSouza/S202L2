from pymongo import MongoClient
from database.model import PersonModel

# Making a connection with MongoClient
client = MongoClient("mongodb://localhost:27017/")

# Getting a database
db = client["person"]

# Getting a collection
collection = db.person

person_model = PersonModel(db)

id_pessoa = person_model.create_person("João Silva", 30)

pessoa = person_model.read_person_by_id(id_pessoa)

person_model.update_person(id_pessoa, "Maria Silva", 35)

person_model.delete_person(id_pessoa)