from src.game.models.models import GameUser
from src.game.repository.GameUserRepository import GameUserRepository
from src.auth.business.AuthBusiness import AuthBusiness
from src.auth.models.User import User
from src.util.Logger import Logger


class GameUserBusiness:

    def __init__(self):
        self.__logger = Logger().get_logger()
        self.__repository = GameUserRepository()
        self.__auth_business = AuthBusiness()

    def add_game_user(self, game_user: GameUser, user: User):
        self.__logger.info(f"User Business add new Game User {game_user.login}")
        self.__auth_business.verify_credentials(user)
        self.__repository.add_game_user(game_user)
