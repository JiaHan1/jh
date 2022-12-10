import app
import requests
import file_operate


class DATA:
    def __init__(self):
        self.url_dataset = app.BASE_URL+'/api/dataset'
        self.url_data_page_list = app.BASE_URL+'/api/dataset/page_list'
        self.url_data_allfiles = app.BASE_URL+'/api/datasetfiles/all_files'
        self.url_dataset_files = app.BASE_URL+'/api/datasetfiles'
        self.url_dataset_copy = app.BASE_URL+'/api/dataset/copy'
        self.url_dataset_delete = app.BASE_URL+'/api/dataset/do_delete'

        # 数据集创建
    def dataset(self, json):
        return requests.post(url=self.url_dataset, headers=file_operate.extract('token', 'app'), data=json,
                             verify=False)

        # 查看数据集
    def data_page_list(self, json):
        return requests.get(url=self.url_data_page_list, headers=file_operate.extract('token', 'app'),
                            data=json, verify=False)

        # 查看数据集中待选文件
    def dataset_files(self, json):
        return requests.get(url=self.url_data_allfiles, headers=file_operate.extract('token', 'app'),
                            params=json, verify=False)

        # 数据集文件添加到训练集，评估集
    def datasetfiles(self, json):
        return requests.post(url=self.url_dataset_files, headers=file_operate.extract('token', 'app'),
                             data=json, verify=False)

        # 复制数据集
    def dataset_copy(self, json):
        return requests.post(url=self.url_dataset_copy, headers=file_operate.extract('token', 'app'), data=json,
                             verify=False)

        # 删除数据集
    def data_delete(self, json):
        return requests.post(url=self.url_dataset_delete, headers=file_operate.extract('token', 'app'),
                             data=json, verify=False)
