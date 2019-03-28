from src.auth.business.AuthBusiness import AuthBusiness, UserAuthenticationService
from src.auth.exceptions.UserAuthenticationException import UserAuthenticationException
from src.auth.models.User import User
from requests.models import Response
from pytest_mock import mocker
import pytest


class TestAuthBusiness:

    def setup(self):
        self.__user = User({"login": "login", "access_token": "access_token"})
        self.__auth_business = AuthBusiness()

    def test_should_pass_on_verify_credentials(self, mocker):
        mocker.patch.object(UserAuthenticationService, 'request_user_authentication')

        response = Response()
        response.status_code = 200

        UserAuthenticationService.request_user_authentication.return_value = response

        self.__auth_business.verify_credentials(self.__user)

        UserAuthenticationService.request_user_authentication.assert_called_with(self.__user)

    def test_should_not_pass_on_verify_credentials(self, mocker):
        mocker.patch.object(UserAuthenticationService, 'request_user_authentication')

        response = Response()
        response.status_code = 401

        UserAuthenticationService.request_user_authentication.return_value = response

        with pytest.raises(UserAuthenticationException):
            self.__auth_business.verify_credentials(self.__user)


