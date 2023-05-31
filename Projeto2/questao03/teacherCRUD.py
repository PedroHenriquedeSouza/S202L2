class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create_teacher(self, nome, ano_nasc, cpf):
        query = "CREATE (:Teacher {nome: $nome, ano_nasc:$ano_nasc, cpf:$cpf})"
        parameters = {"nome": nome, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def read_teacher(self, nome):
        query = "MATCH (t:Teacher{nome:$nome}) RETURN t.nome AS nome, t.ano_nasc AS nascimento, t.cpf AS cpf LIMIT 1"
        parameters = {"nome": nome}
        results = self.db.execute_query(query)
        if len(results) > 0:
            return [result["nome"] for result in results]

    def delete_teacher(self, nome):
        query = "MATCH (t:Teacher {nome: $nome}) DETACH DELETE t"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def update_teacher(self, nome, novo_cpf):
        query = "MATCH (t:Teacher {nome: $nome}) SET t.cpf = $novo_cpf"
        parameters = {"nome": nome, "novo_cpf": novo_cpf}
        self.db.execute_query(query, parameters)