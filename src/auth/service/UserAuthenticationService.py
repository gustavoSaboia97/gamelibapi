from src.auth.models.User import User
from src.auth.configuration.AuthConfiguration import AuthConfiguration
from json import dumps
from requests import Response
import requests


class UserAuthenticationService:

    def __init__(self):
        self.__auth_config = AuthConfiguration()
        self.__headers = {'Content-Type': "application/json"}

    def request_user_authentication(self, user: User) -> Response:
        return requests.post(self.__auth_config.user_api_token_authenticator,
                             data=dumps(user.to_dict()),
                             headers=self.__headers)
