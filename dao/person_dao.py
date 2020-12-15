from dao.dao import DAO
import hashlib


class UserExistsError(Exception):
    pass


class UsernameNotFoundError(Exception):
    pass


class PersonDAO(DAO):

    @staticmethod
    def encrypt_password(password):
        return hashlib.md5(password.encode()).hexdigest()

    @staticmethod
    def is_password_correct(username, password):
        encrypted_password = PersonDAO.encrypt_password(password)
        result = DAO.select("SELECT * FROM person WHERE username = '{}' and password = '{}'".format(username, encrypted_password))
        return len(result) != 0

    @staticmethod
    def get_person_by_username(username):
        result = DAO.select("SELECT * FROM person WHERE username = '{}'".format(username))
        if len(result) == 0:
            raise UsernameNotFoundError("Username was not found")
        return result[0]
