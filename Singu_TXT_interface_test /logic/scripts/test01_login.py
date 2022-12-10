from api.login import LoginAPI
import file_operate


def login():
    login_api = LoginAPI()
    res = login_api.login({'first_name': 'interface', 'password': '123456789'})
    print(res.json())
    file_operate.save(res.json())
    return res


if __name__ == '__main__':
    pass
