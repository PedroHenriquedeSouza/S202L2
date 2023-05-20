from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.211.50.233:7687", "neo4j", "fireball-carts-compromises")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
game_db = GameDatabase(db)

# Criando algumas aulas e suas relações com os professores
game_db.create_match("1", "2x4")
game_db.create_match("2", "5x1")

# Criando alguns jogadores
game_db.create_player("João")
game_db.create_player("Maria")
game_db.create_player("José")
game_db.create_player("Paulo")
game_db.create_player("Davi")

# Atualizando o nome de um jogador
game_db.update_player("João", "Pedro")

# Deletando um jogador e uma partida
game_db.delete_player("5")
game_db.delete_match("2")

# Print de todas as informações do banco de dados
print("Jogadores:")
print(game_db.get_players())
print("Match:")
print(game_db.get_match())
print("Histórico Jogador:")
print(game_db.get_players_list())

# Fechando a conexão
db.close()