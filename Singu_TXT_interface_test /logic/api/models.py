import app
import file_operate
import requests


class MODEL:
    def __init__(self):
        self.url_info = app.BASE_URL+'/api/trainingBatch/info'
        self.url_trainingBatch = app.BASE_URL+'/api/trainingBatch'
        self.url_async_training = app.BASE_URL+'/api/trainingBatch/{}/async_training'\
            .format(file_operate.extract_data('training_batch_id',  'training_batch_id')['training_batch_id'])
        self.headers = file_operate.extract('app',  'token')
        
    # 模型信息
    def model_info(self, json):
        return requests.get(url=self.url_info, headers=self.headers, params=json, verify=False)
    
    # 创建模型
    def training_batch(self, json):
        return requests.post(url=self.url_trainingBatch,  headers=self.headers, json=json, verify=False)
    
    # 模型训练
    def async_training(self):
        return requests.post(url=self.url_async_training, headers=self.headers, verify=False)
