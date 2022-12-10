import app
import file_operate
import requests


class Detail:
    def __init__(self):
        self.URL_labels = app.BASE_URL+'/api/labels'

    # 分类接口
    def class_revise(self, json):
        return requests.post(url=self.URL_labels, headers=file_operate.extract('app', 'token'), json=json, verify=False)
