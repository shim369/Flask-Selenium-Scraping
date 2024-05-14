class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @staticmethod
    def get_login_info():
        return User("shim@gmail.com", "abcd1234")
