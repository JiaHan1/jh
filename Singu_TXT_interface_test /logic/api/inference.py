import app
import requests
import file_operate
import json


class INFERENCE:
    def __init__(self):
        self.headers = file_operate.extract('app', 'token')
        self.url_inference_original = app.BASE_URL+'/api/original'
        self.url_inference_predictfile = app.BASE_URL+'/api/predictfile'
        self.url_delete = app.BASE_URL+'/api/results/do_delete'
        self.url_del_file = app.BASE_URL+'/api/original/do_delete'

        # 上传预测文件
    def inference_original(self, files, data):
        return requests.post(url=self.url_inference_original, files=files, data=data,
                             headers=self.headers, verify=False)

        # 获取预测文件id
    def inference_predictfile_id(self):
        return requests.get(url=self.url_inference_predictfile, headers=self.headers, verify=False)

    def del_inference_file(self, jsons):
        return requests.post(self.url_del_file, headers=self.headers, json=jsons, verify=False)

        # 预测文件
    def inference_file(self):
        path = app.base_dir+'/files/data_inference_file.json'
        with open(path, 'r+', encoding='utf-8') as r:
            data_inference = json.loads(r.read())
            url_inference_file = app.BASE_URL + '/api/original/{}/async_predict'\
                .format(data_inference['list'][0]['id'])
            res_inference = requests.post(url=url_inference_file, headers=self.headers, verify=False)
        print(res_inference.json())
        return res_inference

    # 删除预测文件记录
    def do_delete(self, jsons):
        return requests.post(url=self.url_delete, headers=self.headers, json=jsons, verify=False)


if __name__ == '__main__':
    inference = INFERENCE()
    inference.inference_predictfile_id()
    inference.inference_file()
