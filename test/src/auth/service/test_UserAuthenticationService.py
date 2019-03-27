from src.auth.service.UserAuthenticationService import UserAuthenticationService
from src.auth.models.User import User

from src.auth.service.UserAuthenticationService import requests, AuthConfiguration
from requests.models import Response
from json import dumps
from pytest_mock import mocker


class TestUserAuthenticationService:

    def setup(self):
        self.__user = User({"login": "login", "access_token": "access_token"})
        self.__headers = {'Content-Type': "application/json"}
        self.__user_auth_service = UserAuthenticationService()

    def test_should_create_request_to_user_api(self, mocker):
        mocker.patch.object(AuthConfiguration, 'user_api_token_authenticator')
        mocker.patch.object(requests, 'post')

        auth_config = AuthConfiguration()

        response = Response()
        response.status_code = 200

        requests.post.return_value = response

        response = self.__user_auth_service.request_user_authentication(self.__user)

        requests.post.assert_called_with(auth_config.user_api_token_authenticator,
                                         data=dumps(self.__user.to_dict()),
                                         headers=self.__headers)
        assert response.status_code == 200
