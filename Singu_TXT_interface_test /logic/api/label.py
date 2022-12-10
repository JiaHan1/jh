import app
import requests
import file_operate


class Labelapi:
    def __init__(self, processed_id=None):
        self.URL_MARKED = app.BASE_URL+'/api/processed/{}/marked'.format(processed_id)
        self.URL_get_file_content = app.BASE_URL+'/api/marked/get_file_content_have_id'

    # 提交标注文件
    def marked(self, json):
        return requests.post(url=self.URL_MARKED, json=json, headers=file_operate.extract('token', 'app'), verify=False)

    # 获取文件内容
    def get_file_content(self, data):
        return requests.get(url=self.URL_get_file_content, headers=file_operate.extract('token', 'app'), params=data,
                            verify=False)
