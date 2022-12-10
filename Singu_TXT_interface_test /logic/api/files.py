import requests
import app
import file_operate


class FilesAPI:
    def __init__(self):
        self.url_upload_file = app.BASE_URL+'/api/original/upload_and_process'
        self.url_import_file = app.BASE_URL+'/api/original/import_zip'
        self.url_process_file = app.BASE_URL+'/api/processed/async_process'
        self.url_delete_file = app.BASE_URL+'/api/original/do_delete'
        self.url_page_list = app.BASE_URL+'/api/original/page_list'
        self.url_dispatch_files = app.BASE_URL+'/api/processed/dispatch_files'
        self.HEADERS = file_operate.extract('app', 'token')

    # 上传文件
    def upload_file(self, files, data):
        return requests.post(url=self.url_upload_file, files=files, data=data, headers=self.HEADERS, verify=False)

    # 导入文件
    def import_file(self, import_file):
        return requests.post(url=self.url_import_file, json=import_file, headers=self.HEADERS, verify=False)

    # 预处理文件
    def process_file(self, process_file):
        return requests.post(url=self.url_process_file, json=process_file, headers=self.HEADERS, verify=False)

    # 删除文件
    def delete_file(self, delete_file):
        return requests.post(url=self.url_delete_file, json=delete_file, headers=self.HEADERS, verify=False)

    # 文件信息查询
    def page_list(self, headers):
        return requests.get(url=self.url_page_list, headers=headers, verify=False)

    # 分发文件
    def dispatch_files(self, data):
        return requests.post(url=self.url_dispatch_files,  json=data,  headers=self.HEADERS,  verify=False)
