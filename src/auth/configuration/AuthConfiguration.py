import os


class AuthConfiguration:

    def __init__(self):
        self.__user_api = os.environ.get("USER_API_URL")
        self.__token_uri = "/api/user/login/validate/"

    @property
    def user_api_token_authenticator(self):
        return self.__user_api + self.__token_uri
