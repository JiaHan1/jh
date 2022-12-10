import requests
import app
import file_operate


class Qualitycheck:
    def __init__(self):
        self.url_check_file = app.BASE_URL+'/api/marked/check_file'
        self.url_files_to_check = app.BASE_URL+'/api/marked/files_to_check'

    # 获取文件
    def files_to_check(self):
        return requests.get(url=self.url_files_to_check, headers=file_operate.extract('token', 'app'), verify=False)

    # 质检文件
    def check_file(self, json):
        return requests.post(url=self.url_check_file, headers=file_operate.extract('token', 'app'),
                             data=json, verify=False)
