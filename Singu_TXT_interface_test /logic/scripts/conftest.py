import pytest
from api.login import LoginAPI
import file_operate


@pytest.fixture(scope='class')
def init():
    login = LoginAPI()
    res_login = login.login({'first_name': 'interface', 'password': '123456789'})
    print('login:  ', res_login)
    file_operate.save(res_login.json())
