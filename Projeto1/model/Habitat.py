import json
from model.Cuidador import Cuidador

class Habitat:
    def __init__(self, id, nome, tipoAmbiente, cuidador: Cuidador):
        self.id = id
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador.__dict__
    
    def toJSON(self):
        return json.dumps(self.__dict__, check_circular=True)