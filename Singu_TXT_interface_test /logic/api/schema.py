import app
import file_operate
import requests


class Schema:
    def __init__(self):
        self.URL_schema = app.BASE_URL+'/api/schema'

    # 改变元素
    def schema_revise(self, json):
        return requests.post(url=self.URL_schema, headers=file_operate.extract('app', 'token'), json=json, verify=False)
