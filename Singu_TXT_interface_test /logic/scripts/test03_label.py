import random
from api.label import Labelapi
import file_operate
from scripts.test02_files import page_list


# 调用获取html元素接口
def get_file_content():
    label_api = Labelapi()
    data_r = file_operate.open_file_r('content_file')
    res_list = list()
    for i in data_r:
        res_get_file_content = label_api.get_file_content({"processed_file_id": i['processed_id']})
        res_list.append(res_get_file_content)
        print('【res_get_file_content】', res_get_file_content.text)
        if res_get_file_content.status_code == 200:
            i['html'] = res_get_file_content.json()['html']
            file_operate.open_file_w('content_file', data_r)
    return res_list


# 读取content文件的内容，提交标注到质检
def label():
    page_list()
    label_api = Labelapi()
    data_r = file_operate.open_file_r('content_file')
    class_r = file_operate.try_open('data_class')
    class_id_list = [i['id'] for i in class_r if 'id' in i.keys()]
    label_data = dict()
    if class_id_list:
        class_id = random.choice(class_id_list)
        label_data['label_id'] = class_id
    res_list = list()
    for i in data_r:
        if 'html' in i.keys():
            print(i['processed_id'])
            label_api.__init__(i['processed_id'])
            label_data['html'] = i['html']
            res_label = label_api.marked(label_data)
            res_list.append(res_label)
            print('【res_label】', res_label.text)
    return res_list


if __name__ == "__main__":
    label()
    get_file_content()
