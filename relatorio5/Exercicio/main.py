from database.database import Database
from database.model import BookModel
from helper.save_json import writeAJson

db = Database(database="library", collection="books")
data = db.collection.find()
book_model = BookModel(db)

id_book1 = book_model.create_book("Moby Dick", "Herman Melville", 1851, 25.0)  
id_book2 = book_model.create_book("1984", "George Orwell", 1949, 20.0) 
id_book3 = book_model.create_book("Harry Potter e o Prisioneiro de Asaban", "JK Rowlin", 2023, 50.0)

book1 = book_model.read_book_by_id(id_book1)
book2 = book_model.read_book_by_id(id_book2)
book3 = book_model.read_book_by_id(id_book3)

writeAJson((book1,book2, book3), "library")

book_model.update_book(id_book3, "Harry Potter e o Prisioneiro de Askaban", "JK Rowling", 2004, 35.90)

book_model.delete_book(id_book2)