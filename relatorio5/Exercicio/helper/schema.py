book_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["titulo", "autor", "ano", "preco"],
        "properties": {
            "titulo": {
                "bsonType": "string",
                "descricao": "O titulo deve ser do tipo string"
            },
            "autor": {
                "bsonType": "string",
                "descricao": "O autor deve ser do tipo string"
            },
            "ano": {
                "bsonType": "int",
                "minimo": 1500,
                "maximo": 2023,
                "descricao": "O ano deve ser do tipo int"
            },
            "preco": {
                "bsonType": "double",
                "descricao": "O preco deve ser do tipo double"
            }
        }
    }
}