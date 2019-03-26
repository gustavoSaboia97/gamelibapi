from src.auth.configuration.AuthConfiguration import AuthConfiguration
import os


class TestAuthConfiguration:

    def setup(self):
        os.environ["USER_API_URL"] = "http://localhost:8080"
        self.__auth_config = AuthConfiguration()

    def test_should_return_token_endpoint(self):
        assert "http://localhost:8080/api/user/login/validate/" == self.__auth_config.user_api_token_authenticator
