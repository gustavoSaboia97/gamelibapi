from src.auth.service.UserAuthenticationService import UserAuthenticationService
from src.auth.models.User import User
from src.auth.exceptions.UserAuthenticationException import UserAuthenticationException


class AuthBusiness:

    def __init__(self):
        self.__user_auth_service = UserAuthenticationService()

    def verify_credentials(self, user: User):
        response = self.__user_auth_service.request_user_authentication(user)
        if not response.status_code == 200:
            raise UserAuthenticationException()

