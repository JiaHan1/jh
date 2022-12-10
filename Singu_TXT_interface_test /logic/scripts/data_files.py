import os
import json
from api.datasets import DATA
import file_operate


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


# 创建数据集
def dataset():
    datas = DATA()
    w_data = file_operate.try_open('data_infor')
    if not w_data:
        file_operate.open_file_w('data_infor', [{'name': 'data1'}])
        w_data = file_operate.try_open('data_infor')
    datasets = [i for i in w_data if i['name'][4:] not in 'copy']
    name = datasets[-1].copy()
    num = name['name'][4:]
    num = int(num) + 1
    print('w1', w_data)
    name['name'] = 'data' + str(num)
    print(name['name'])
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


if __name__ == "__main__":
    dataset()
