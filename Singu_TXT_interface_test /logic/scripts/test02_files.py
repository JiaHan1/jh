import time
from api.files import FilesAPI
import json
import file_operate
import app
import os


# 上传预处理文件
def upload_file():
    files_api = FilesAPI()
    path_files = app.base_dir+'/files/files_01'
    format_file = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'xml', 'txt', 'html', 'png', 'jpg', 'jpeg', 'bmp',
                   'tif', 'tiff']
    res_list = list()
    for path, dirs, files_name in os.walk(path_files):
        for file in files_name:
            if os.path.splitext(file)[1].replace('.', '') in format_file:
                files = {'files': (file, open(path+'/'+file, mode='rb').read(), "multipart/form-data")}
                data = {"file_type": "1"}
                page_list()
                try:
                    data_w = file_operate.open_file_r('upload_file')
                    for i in data_w:
                        if file == i['filename']:
                            delete_file(file)
                except Exception as e:
                    print(e)
                res_upload_file = files_api.upload_file(files, data)
                res_list.append(res_upload_file)
                time.sleep(1)
                print('[upload_file_res]:       ', res_upload_file.json())
    return res_list


def delete_file(file_name='false'):
    files_api = FilesAPI()
    if file_name == 'false':
        return
    else:
        path_file = app.base_dir + '/files/upload_file.json'
        with open(path_file, 'r+', encoding='utf-8') as f_r:
            try:
                data_r = file_operate.open_file_r('upload_file')
            except Exception as e:
                print('没有文件可删除', e)
            data_del = []
            for i in data_r:
                if i['filename'] == file_name:
                    ids = i['id']
                else:
                    data_del.append(i)
                files_api.delete_file({"ids": [ids]})
            data_str = json.dumps(data_del, indent=8, ensure_ascii=False)
            f_r.seek(0)
            f_r.truncate()
            f_r.write(data_str)


# 获取原文件信息，实时写入json文件，查重，替换
def page_list():
    files_api = FilesAPI()
    while True:
        res_page = files_api.page_list(file_operate.extract('token', 'app'))
        if res_page.status_code == 200:
            state = [int(i['state']) for i in res_page.json()['list']]
            if all(i not in (1, 2, 3) for i in state):
                break
        else:
            break
    file_operate.open_file_w('upload_file', res_page.json()['list'])
    file_operate.open_file_w('content_file', res_page.json()['list'])
    print('【res_page】', res_page.json())
    return res_page


# 分发所有文件
def dispatch_files():
    files_api = FilesAPI()
    page_list()
    data_r = file_operate.open_file_r('content_file')
    processed_id_list = [i['processed_id'] for i in data_r]
    processed_file_id = {"processed_file_id_list": processed_id_list}
    processed_file_id.update(file_operate.extract('operator_id'))
    res_dispatch_files = files_api.dispatch_files(processed_file_id)
    print('【res_dispatch_files】=       ', res_dispatch_files.text)
    return res_dispatch_files


if __name__ == '__main__':
    # upload_file()
    # page_list()
    dispatch_files()
