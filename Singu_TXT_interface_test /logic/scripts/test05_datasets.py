import json
from api.datasets import DATA
import file_operate
import os


# 查看数据集所有文件，保存到json文件中，查重，替换最新数据
def dataset():
    datas = DATA()
    w_data = file_operate.try_open('data_infor')
    if not w_data:
        file_operate.open_file_w('data_infor', [{'name': 'data1'}])
        w_data = file_operate.try_open('data_infor')
    datasets = [i for i in w_data if 'copy' not in i['name'][4:] ]
    name = datasets[-1].copy()
    num = name['name'][4:]
    num = int(num) + 1
    name['name'] = 'data' + str(num)
    res_dataset = datas.dataset(name)
# 数据集名称重复，重新编写名称
    if res_dataset.status_code != 200:
        while True:
            if '同名' in res_dataset.json()['message']:
                num = num+1
                name['name'] = 'data' + str(num)
                res_dataset = datas.dataset(name)
                print('报错', res_dataset.json())
            else:
                break
    else:
        w_data.append(res_dataset.json())
    file_operate.open_file_w('data_infor', w_data)
    print(res_dataset.text)
    return res_dataset


# 复制数据集，保存到json文件中，查重，替换最新数据
def dataset_copy():
    data = DATA()
    w_data = file_operate.try_open('data_infor')
    if not w_data:
        dataset()
        w_data = file_operate.open_file_r('data_infor')
    datasets = [i for i in w_data if 'copy' not in i['name'][4:]]
    data_name_copy = [i for i in w_data if 'copy' in i['name'][4:]]
    data_copy_value = [i['name'] for i in data_name_copy]
    name_copy = dict()
    name_copy['name'] = str(datasets[-1]['name']) + 'copy'
    res_dataset_copy = data.dataset_copy({'dataset': str(datasets[-1]['id']), 'name': name_copy['name']})
    print(res_dataset_copy.json())
    if 'error_code' not in res_dataset_copy.json().keys():
        w_data.append(name_copy)
    if '数据集同名' in res_dataset_copy.json()['message']:
        for i_data in w_data:
            if 'id' in i_data.keys():
                name_copy = i_data.copy()
                name_copy['name'] = str(i_data['name'])+'copy'
                print(name_copy)
                if name_copy['name'] not in data_copy_value:
                    print('3')
                    break
        print(data_copy_value)
        res_dataset_copy = data.dataset_copy({'dataset': str(name_copy['id']), 'name': str(name_copy['name'])})
        w_data.append(name_copy)
        print('2')
    elif '数据集不存在' in res_dataset_copy.json()['message']:
        dataset()
    else:
        w_data.append(name_copy)
    file_operate.open_file_w('data_infor', w_data)
    print(res_dataset_copy.json())
    return res_dataset_copy


# 查看数据集信息
def data_page_list():
    data = DATA()
    res_data_page_list = data.data_page_list({'page': 1})
    print(res_data_page_list.text)
    return res_data_page_list


# 删除数据集，把json文件的数据集信息一并删除，更新
def data_del():
    data = DATA()
    r_data = file_operate.try_open('data_infor')
    if not r_data:
        dataset()
        r_data = file_operate.open_file_r('data_infor')
    r_data_edit = [i for i in r_data if 'can_edit' in i.keys()]
    id_json = [i['id'] for i in r_data_edit if i['can_edit'] is True]
    res_data_del = data.data_delete(id_json[0])
    data_infor_del = [i for i in r_data if i['id'] != id_json[0]]
    if data_infor_del:
        file_operate.open_file_w('data_infor', data_infor_del)
    print('[res_data_del]', res_data_del.json())
    return res_data_del


# 查看数据集所有文件，保存到json文件中，查重，替换最新数据
def dataset_all_files():
    data = DATA()
    res_dataset_all_files = data.dataset_files({'dataset': file_operate.extract_data('data_infor', 'id').get('id')})
    print('[res_dataset_all_files]', res_dataset_all_files.json())
    try:
        files = {}
        file_num = 0
        path_data_files = os.path.abspath('../files/data_files.json')
        with open(path_data_files, 'r+', newline='\n', encoding='utf-8') as r:
            for file_infor in res_dataset_all_files.json()['list']:
                files[str(file_num)] = file_infor
                file_num += 1
            r.seek(0)
            r.truncate()
            r.write(json.dumps(files, indent=8, ensure_ascii=False))
    except Exception as e:
        raise ValueError(e)
    return res_dataset_all_files


# 文件放入训练数据集
def dataset_training_files():
    data = DATA()
    file_id_list = []
    num = 0
    for i in range(0, 6):
        i = '{}'.format(i)
        file_id = file_operate.extract_data('data_files', i).get(i)
        if file_id is not None:
            num += 1
            print('有{}个文件放到训练集'.format(num))
            file_id_list.append(file_id['marked_file_id'])
            print(file_id_list)
    res_dataset_training_files = data.datasetfiles({'dataset': file_operate.extract_data('data_infor', 'id').get('id'),
                                                    'training_files': str(file_id_list)})
    print('[res_dataset_training_files]', res_dataset_training_files.json())
    return res_dataset_training_files


# 把待选列表的文件放入测试数据集
def dataset_testing_files():
    data = DATA()
    data_infor = "data_infor"
    data_files = "data_files"
    file_id_list = []
    num = 0
    for i in range(6):
        i = '{}'.format(i)
        file_id = file_operate.extract_data(data_files, i).get(i)
        if file_id is not None:
            num += 1
            print('有{}个文件放到测试集'.format(num))
            file_id_list.append(file_id['marked_file_id'])
    res_dataset_training_files = data.datasetfiles({'dataset': file_operate.extract_data(data_infor, 'id').get('id'),
                                                    'predict_files': str(file_id_list)})
    print(res_dataset_training_files.json())
    return res_dataset_training_files


if __name__ == "__main__":

    dataset()
    # dataset_copy()
    # dataset_all_files()
