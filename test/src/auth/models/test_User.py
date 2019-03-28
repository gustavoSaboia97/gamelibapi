from src.auth.models.User import User


class TestUser:

    def setup(self):
        self.__user = User({"login": "login", "access_token": "access_token"})

    def test_should_set_the_correct_data(self):
        assert self.__user.login == "login"
        assert self.__user.access_token == "access_token"
