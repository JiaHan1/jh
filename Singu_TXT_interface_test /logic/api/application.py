import app
import requests
import file_operate


class APP:
    def __init__(self):
        self.URL_application = app.BASE_URL+'/api/application'
        self.HEADERS = file_operate.extract('token')

    # 创建应用
    def application(self, json):
        return requests.post(url=self.URL_application, headers=self.HEADERS, json=json, verify=False)
