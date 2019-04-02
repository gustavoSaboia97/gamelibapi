from src.game.configuration.MongoConfiguration import MongoConfiguration
from src.game.models.models import GameUser
from src.util.Logger import Logger


class GameUserRepository:

    def __init__(self):
        self.__mongo_configuration = MongoConfiguration()
        self.__database = self.__mongo_configuration.database
        self.__game_user_collection = self.__database.game_user_collection
        self.__logger = Logger().get_logger()

    def add_game_user(self, game_user: GameUser) -> GameUser:
        self.__logger.info(f"Inserting new user in the system {game_user.login}")
        self.__game_user_collection.insert_one(game_user.to_mongo_dict())
