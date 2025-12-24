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

user1 = UserAccount("mail", "email", "password")

#pw = input("Введите новый пароль: ")
#print(user1.set_password(pw))

user_input = input("Введите пароль для проверки: ")
if user1.check_password(user_input):
    print("Пароль верный")
else:
    print("Неверный пароль")
print(user1.get_account_info())
