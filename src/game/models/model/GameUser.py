from src.game.models.model.Game import Game


class GameUser:

    def __init__(self, user_id: str, login: str, games: list):
        self.__user_id = user_id
        self.__login = login
        self.__games = games

    @property
    def user_id(self):
        return self.__user_id

    @property
    def login(self):
        return self.__login

    @property
    def games(self):
        return self.__games

    def to_dict(self) -> dict:
        return {
            "id": self.__user_id,
            "login": self.__login,
            "games": self.__games
        }

    def to_mongo_dict(self) -> dict:
        return {
            "_id": self.__user_id,
            "login": self.__login,
            "games": self.__games
        }
