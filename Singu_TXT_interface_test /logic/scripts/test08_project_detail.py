import random
from api.detail import Detail
import file_operate


def class_add():
    detail = Detail()
    data_class = file_operate.try_open('data_class')
    class_name = [i['name'] for i in data_class]
    datas = data_class.copy()
    for i in range(3):
        while True:
            class_three = '分类' + str(random.randint(-1000000000000, 10000000000000))
            if class_three not in class_name:
                datas.append({'name': class_three})
                print(datas)
                break
    class_data_list = dict(labels=datas)
    res_add_class = detail.class_revise(class_data_list)
    if res_add_class.status_code == 200:
        for i in res_add_class.json():
            if type(i) == dict:
                if 'id' in i.keys():
                    data_class.append(i)
    print(data_class)
    print('【res_add_class】', res_add_class.json())
    file_operate.open_file_w('data_class', data_class)
    return res_add_class


def class_rename():
    detail = Detail()
    data_class = file_operate.try_open('data_class')
    if data_class:
        pass
    else:
        class_add()
    data_class = file_operate.try_open('data_class')
    datas = data_class.copy()
    class_name = [i['name'] for i in data_class]
    while True:
        name = random.choices(class_name)
        name = ''.join(name)+'改'
        if name not in class_name:
            # data_class_del = [i for i in data_class if i['name'] != name]
            break
    name_data_dict = {'name': name}
    data_class.append(name_data_dict)
    class_data_dict = {'labels': data_class}
    res_class_rename = detail.class_revise(class_data_dict)
    if res_class_rename.status_code == 200:
        for i in res_class_rename.json():
            if 'id' in i.keys():
                datas.append(i)
        file_operate.open_file_w('data_class', datas)
    print('【res_class_rename】', res_class_rename.json())
    return res_class_rename


def class_del():
    detail = Detail()
    while True:
        data_class = file_operate.try_open('data_class')
        if len(data_class) < 8:
            class_add()
        else:
            break
    class_name = [i['name'] for i in data_class]
    name_list = []
    for i in range(3):
        name = random.choices(class_name)
        name = ''.join(name)
        if name not in name_list:
            name_list.append(name)
    class_name_del = [item for item in data_class if item["name"] not in name_list]
    class_data_dict = {'labels': class_name_del}
    res_class_del = detail.class_revise(class_data_dict)
    if res_class_del.status_code == 200:
        file_operate.open_file_w('data_class', class_name_del)
    print('【res_class_del】', res_class_del.json())
    return res_class_del
# class_del()


def class_remove():
    detail = Detail()
    res_class_del = detail.class_revise({'labels': []})
    file_operate.open_file_w('data_class', [])
    print('【res_class_remove】', res_class_del.json())
    return res_class_del


if __name__ == "__main__":
    # class_del()
    # class_rename()
    class_add()
    # class_remove()
