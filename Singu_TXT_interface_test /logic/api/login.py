import requests


# 登录
class LoginAPI:
    def __init__(self):
        self.url = "https://120.133.220.180:3000/api/login"

    def login(self, login_data):
        return requests.post(url=self.url, json=login_data, verify=False)
