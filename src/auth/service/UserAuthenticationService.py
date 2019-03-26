from src.auth.models.User import User
from src.auth.configuration.AuthConfiguration import AuthConfiguration
import requests


class UserAuthenticationService:

    def __init__(self, user: User):
        self.__auth_config = AuthConfiguration()
        self.__user = user
        self.__headers = {'Content-Type': "application/json"}

    def request_user_authentication(self):
        return requests.post(self.__auth_config, data=self.__user.to_dict(), headers=self.__headers)
