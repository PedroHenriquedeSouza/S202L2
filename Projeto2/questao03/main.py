from database import Database
from teacherCRUD import TeacherCRUD

db = Database("bolt://18.207.148.220:7687", "neo4j", "carriers-type-stationery")
db.drop_all()

teacher_crud = TeacherCRUD(db)

teacher_crud.create_teacher("Chris Lima", 1956, '189.052.396-66')
teacher_crud.read_teacher("Chris Lima")
teacher_crud.update_teacher("Chris Lima", "162.052.777-77")
teacher_crud.read_teacher("Chris Lima")

db.close()