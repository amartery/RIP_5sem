from abc import ABC, abstractmethod

"""
Фабричный метод — это порождающий паттерн проектирования, 
который решает проблему создания различных продуктов, 
без указания конкретных классов продуктов.
"""


class User(ABC):
    """абстрактный пользователь"""
    pass


class GmailUser(User):
    """пользователь с аккаунтом google"""
    def __init__(self, email):
        print("пользователь с аккаунтом Google: {}".format(email))


class MobileUser(User):
    """пользователь с номером мобильного телефона"""
    def __init__(self, phone_number):
        print("пользователь c номером телефона: {}".format(phone_number))


class FacebookUser(User):
    """пользователь с почтой rambler"""
    def __init__(self, facebook_nickname):
        print("пользователь с аккаунтом Facebook: {}".format(facebook_nickname))


class Credentials(ABC):
    """абстрактные учетные данные"""
    pass


class GmailCredentials(Credentials):
    """учетные данные для входа с помощью аккаунта Google"""
    def __init__(self, email, password):
        self._email = email
        self._password = password

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password


class MobileCredentials(Credentials):
    """учетные данные для входа с помощью номера телефона"""
    def __init__(self, phone_number, password):
        self._phone_number = phone_number
        self._password = password

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def password(self):
        return self._password


class FacebookCredentials(Credentials):
    """учетные данные для входа с помощью номера телефона"""
    def __init__(self, facebook_nickname, password):
        self._facebook_nickname = facebook_nickname
        self._password = password

    @property
    def facebook_nickname(self):
        return self._facebook_nickname

    @property
    def password(self):
        return self._password


class Authenticator(ABC):
    """абстрактный аутентификатор"""
    @abstractmethod
    def authenticate(self, credentials: Credentials) -> User:
        pass


class GmailAuthenticator(Authenticator):
    """аутентификатор Gmail"""
    def authenticate(self, credentials: GmailCredentials) -> GmailUser:
        print("аутентицирован с помощью аккаунта Google: {}\n"
              "был введен пароль: {}".format(credentials.email, credentials.password))
        return GmailUser(credentials.email)


class MobileAuthenticator(Authenticator):
    """аутентификатор Mobile"""
    def authenticate(self, credentials: MobileCredentials) -> MobileUser:
        print("аутентицирован с помощью номера мобильного телефона: {}\n"
              "был введен пароль: {}".format(credentials.phone_number, credentials.password))
        return MobileUser(credentials.phone_number)


class FacebookAuthenticator(Authenticator):
    """аутентификатор Facebook"""
    def authenticate(self, credentials: FacebookCredentials) -> FacebookUser:
        print("аутентицирован с помощью аккаунта Facebook: {}\n"
              "был введен пароль: {}".format(credentials.facebook_nickname, credentials.password))
        return FacebookUser(credentials.facebook_nickname)


def authenticate_user(authenticator: Authenticator, credentials: Credentials) -> User:
    return authenticator().authenticate(credentials)


if __name__ == '__main__':

    gmail_email = "123@gmail.com"
    gmail_password = "qwerty"
    gmail_credentials = GmailCredentials(gmail_email, gmail_password)
    gmail_user: GmailUser = authenticate_user(GmailAuthenticator, gmail_credentials)

    print()

    mobile_phone_number = "+79042946789"
    mobile_password = "qwerty904"
    mobile_credentials = MobileCredentials(mobile_phone_number, mobile_password)
    mobile_user: MobileUser = authenticate_user(MobileAuthenticator, mobile_credentials)

    print()

    facebook_name = "programmer123"
    facebook_password = "asdfg"
    facebook_credentials = FacebookCredentials(facebook_name, facebook_password)
    facebook_user: FacebookUser = authenticate_user(FacebookAuthenticator, facebook_credentials)

