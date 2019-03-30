class User:

    def __init__(self, user: dict):
        self.__login = user["login"]
        self.__access_token = user["access_token"]

    @property
    def login(self) -> str:
        return self.__login

    @property
    def access_token(self) -> str:
        return self.__access_token

    def to_dict(self) -> dict:
        return {
            "login": self.__login,
            "access_token": self.__access_token
        }
