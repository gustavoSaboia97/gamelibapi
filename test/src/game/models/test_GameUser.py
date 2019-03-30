from src.game.models.model.GameUser import GameUser


class TestGameUser:

    def setup(self):
        self.__user_id = "user_id"
        self.__login = "login"
        self.__games = list()
        self.__game_user = GameUser(self.__user_id, self.__login, self.__games)

    def test_should_set_correct_data(self):
        assert self.__game_user.user_id == self.__user_id
        assert self.__game_user.login == self.__login
        assert self.__game_user.games == self.__games
