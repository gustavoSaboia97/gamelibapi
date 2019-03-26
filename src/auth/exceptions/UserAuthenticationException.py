class UserAuthenticationException(Exception):

    def __init__(self):
        Exception.__init__(self)
        self.message = "User Not Authenticated"
        self.status_code = 401
