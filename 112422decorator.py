import json
from functools import wraps


class User:

    def __init__(self, username, password, email, age, phone):
        self.name = username
        self.password = password
        self.email = email
        self.age = age
        self.phone = phone
        self.dict_ = {
            "username": self.name,
            "password": self.password,
            "email": self.email,
            "age": self.age,
            "phone": self.phone
        }

        with open("database_user.json", "r") as users:
            file = json.load(users)
            file.append(self.dict_)
        with open("database_user.json", "w") as add:
            json.dump(file, add)


class PyRequest:
    def __init__(self, headers=None, authorization=None, body=None, user=None):
        if headers is None:
            headers = []
        self.headers = headers
        self.authorization = authorization
        self.body = body
        self.user = user


def get_user_info(username, password):
    with open("database_user.json") as users:
        user = json.load(users)
        for i in user:
            if i["username"] == username and i["password"] == password:
                print(i)


def login_required(func):
    @wraps(func)
    def decor(username, password):
        if func(username, password) is None:
            raise "401 Unauthorized request error"
        else:
            print(get_user_info(username=username, password=password))

    return decor


@login_required
def local_login(username, password):
    with open("database_user.json") as users:
        user = json.load(users)
        for i in user:
            if username == i["username"] and password == i["password"]:
                return True


local_login(username="Gag", password="gag994556")
