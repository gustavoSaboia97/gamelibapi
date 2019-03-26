from src.auth.service.UserAuthenticationService import UserAuthenticationService
from src.auth.models.User import User


class TestUserAuthenticationService:

    def setup(self):
        self.__user = User({"login": "login", "access_token": "access_token"})
        self.__user_auth_service = UserAuthenticationService(self.__user)

    def test_should_create_request_to_user_api(self):
        pass
