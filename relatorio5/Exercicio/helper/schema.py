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
                "bsonType": "array",
                "items": {
                    "bsonType": "objectId",
                    "descricao": "O autor deve ser do tipo string"
                }
            },
            "ano": {
                "bsonType": "int",
                "minimo": 1500,
                "maximo": 2023,
                "descricao": "O ano deve ser do tipo int"
            },
            "preco": {
                "bsonType": "float",
                "descricao": "O preco deve ser do tipo float"
            }
        }
    }
}