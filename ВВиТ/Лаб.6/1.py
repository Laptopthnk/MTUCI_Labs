class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        return f"Пароль успешно изменен"

    def check_password(self, password):
        return password == self.__password

    def get_account_info(self):
        return f"Username: {self.username}, Email: {self.email} Password: {self.__password}"

