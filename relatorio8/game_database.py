class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, player_name):
        query = "CREATE (p:Player {player_name: $player_name})"
        parameters = {"player_name": player_name}
        self.db.execute_query(query, parameters)

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {player_name: $old_name}) SET p.player_name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)
    
    def delete_player(self, player_name):
        query = "MATCH (p:Player {player_name: $player_name}) DETACH DELETE p"
        parameters = {"player_name": player_name}
        self.db.execute_query(query, parameters)

    def create_match(self, id_match, result):
        query = "CREATE (:Match {id_match: $id_match, result: $result})"
        parameters = {"id_match": id_match, "result": result}
        self.db.execute_query(query, parameters)

    def update_result_match(self, id_match, result):
        query = "MATCH (m:Match {id_match: $id_match}) SET m.result = $result"
        parameters = {"id_match": id_match, "result": result}
        self.db.execute_query(query, parameters)

    def delete_match(self, id_match):
        query = "MATCH (m:Match {id_match: $id_match}) DETACH DELETE m"
        parameters = {"id_match": id_match}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.player_name AS player_name"
        results = self.db.execute_query(query)
        return [result["player_name"] for result in results]

    def get_match(self):
        query = "MATCH (m:Match) RETURN m.result AS result"
        results = self.db.execute_query(query)
        return [result["result"] for result in results]

    def get_players_list(self):
        query = "MATCH (m:Match)<-[:JOGOU_EM]-(p:Player) RETURN p.player_name AS player_name"
        results = self.db.execute_query(query)
        return [result["player_name"] for result in results]