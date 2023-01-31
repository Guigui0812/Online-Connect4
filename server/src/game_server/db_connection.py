import pymongo 

class DBConnection:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["mydatabase"]
        self.players_collection = self.db["players"]
        self.games_collection = self.db["games"]

    def insert_player(self, player):
        self.players_collection.insert_one(player)

    def insert_game(self, game):
        self.games_collection.insert_one(game)

    def disconnect(self):
        self.client.close()