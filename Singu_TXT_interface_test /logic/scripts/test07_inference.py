import time
import json
from api.inference import INFERENCE
import os
import file_operate
import app


# 获取预测文件id，保存到json文件
def inference_predictfile_id():
    inferences = INFERENCE()
    res_inference_files = inferences.inference_predictfile_id()
    if res_inference_files.status_code == 200:
        file_operate.open_file_w('data_inference_file', res_inference_files.json()['list'])
    print(res_inference_files.json())
    return res_inference_files


# 删除预测的文件，同时删除json文件中的文件数据。
def del_inference_file(filename=None):
    inferences = INFERENCE()
    path = app.base_dir + '/files/data_inference_file.json'
    with open(path, 'r+', encoding='utf-8') as r:
        try:
            data_inference = json.loads(r.read())
        except ValueError as e:
            print('没有可删除文件：{},报错'.format(filename, e))
            return
        if filename is None:
            res_del_inference = inferences.del_inference_file({"ids": [data_inference.get('list')[0]['id']]})
            del data_inference.get('list')[0]
        else:
            for file_dict in data_inference:

                if filename == file_dict['filename']:
                    file_id = file_dict['id']
                    res_del_inference = inferences.del_inference_file({"ids": [file_id]})
                    data_inference.remove(file_dict)
                    file_operate.open_file_w('data_inference_file', data_inference)
                    print('【res_del_inference_file】 ', res_del_inference.json())
                    return res_del_inference

                else:
                    print('未找到可删除文件:{}'.format(filename))
                    return True




# 上传预测文件，查重，实时保存到json文件，并且预测。
def inference():
    inferences = INFERENCE()
    path_files = app.base_dir+'/files/files_01'
    file_format = ["pdf", "htm", "txt", "html", "doc", "docx", "xls", "xlsx", "xml", "model", "dict", "pickle", "png",
                   "jpg", "jpeg", "bmp", "tif", "tiff", "zip"]
    for path, dir, files_name in os.walk(path_files):
        for file in files_name:
            if os.path.splitext(file)[1].replace('.', '') in file_format:
                files = {'files': (file, open(path + '/' + file, mode='rb').read(), "multipart/form-data")}
                data = {"app": str(file_operate.extract('app')['app']), "file_type": "8"}
                inference_predictfile_id()
                data_w = file_operate.try_open('upload_file')
                if data_w:
                    for i in data_w:
                        if file == i['filename']:
                            del_inference_file(file)
                else:
                    pass
                # 上传预测文件
                res_inference_original = inferences.inference_original(files, data)
                print('【res_inference_original】', res_inference_original.json())
                # 获取预测文件id
                while True:
                    res_inference_predictfile_infor = inferences.inference_predictfile_id()
                    print(res_inference_predictfile_infor.json())
                    if res_inference_predictfile_infor.status_code == 200:
                        if res_inference_predictfile_infor.json()['list'][0]['state'] == 6:
                            time.sleep(1)
                        else:
                            file_operate.save_data('data_inference_file', res_inference_predictfile_infor.json()
                            ['list'])
                            break
                    else:
                        return res_inference_predictfile_infor
                if res_inference_predictfile_infor.status_code == 200:
                    data_w = file_operate.open_file_r('data_inference_file')
                    for i_file in data_w:
                        if i_file['has_predict'] is True:
                            inferences.do_delete({'ids': [i_file['result_file'][0]['id']]})
                    for i in data_w:
                        if file == i['filename']:
                            del_inference_file(file)
                res_interence_upload_file = inferences.inference_original(files, data)
                if 'error_code' in res_interence_upload_file.json().keys():
                    print(res_interence_upload_file.json())
                    return res_interence_upload_file
                print('【res_interence_upload_file】:       ', res_interence_upload_file.json())
    res_inference_predictfile_infor = inferences.inference_predictfile_id()
    file_operate.save_data('data_inference_file', res_inference_predictfile_infor.json())
    # 进行文件预测
    res_inference_file = inferences.inference_file()
    print('【res_inference_file】:        ', res_inference_file.json())
    return res_inference_file


if __name__ == '__main__':
    inference()
