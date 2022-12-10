import random
import app
from api.schema import Schema
import file_operate
import json


def schema_add():
    schema = Schema()
    list_name = []
    list_name_data = []
    list_name_add = []
    r_data = file_operate.try_open('schema_data')
    if not r_data:
        file_operate.save_data('schema_data', [{'name': "元素1"}])
        r_data = file_operate.try_open('schema_data')
    for name_data in r_data:
        name = name_data
        find_str = '改'
        name_add = {}
        if find_str in name['name']:
            num = int(name['name'][2:name['name'].index(find_str)])
            num += 1
            name_add['name'] = name['name'].replace(name['name'][2:name['name'].index(find_str)], str(num))
        else:
            num = name['name'][2:]
            num = int(num)+1
            name_add['name'] = name['name'].replace(name['name'][2:], str(num))

        list_name_add.append(name_add)
        list_name.append(name['name'])
        list_name_data.append(name)
# 写入json文件的名称去重
    w_name = [i for i in list_name_add if i['name'] not in list_name]
    for data in w_name:
        list_name_data.append(data)
    file_operate.open_file_w('schema_data', list_name_data)
    schema_data_l = []
    for i in list_name_data:
        i.update({"multi": False, "app": file_operate.extract_value('app')})
        schema_data_l.append(i)
    schema_data = {'appId': '129', 'schema': schema_data_l}
    res_shcema_add = schema.schema_revise(schema_data)
    print('[res_shcema_add]', res_shcema_add.json())
    return res_shcema_add


def schema_rename():
    schema = Schema()
    with open(app.base_dir+'/files/schema_data.json', 'r+', encoding='utf-8') as w:
        # 校验字典中是否有值
        r_data = file_operate.open_file_r('schema_data')
        if not r_data:
            file_operate.save_data('schema_data', [{'name': "元素1"}])
            r_data = file_operate.open_file_r('schema_data')
        ran_name = random.choices(r_data, k=3)
        # 对列表的字典进行去重
        rename_r = [dict(r) for r in set([tuple(i.items()) for i in ran_name])]
        for dict_ran_i in rename_r:
            name = dict_ran_i['name']
    # 校验元素名称中是存在'改'字
            if '改' in name:
                index = name.index('改')
                num = int(name[index:])
                num = num + 1
                name = name.replace[name[index:], str(num)]
            else:
                name = name[2:]+'改1'
            dict_name = dict()
            dict_name['name'] = name
            r_data.append(dict_name)
        list_data_name = []
        for data in r_data:
            data_name = data['name']
            if data_name not in list_data_name:
                list_data_name.append(data_name)
                data['multi'] = False
                data['app'] = 129
                shcema_data = {'appId': '129', 'schema': r_data}
        # 写入的时候，名字去重
        name_remove = [i for i in rename_r if i['name'] not in list_data_name]
        if len(name_remove) != 0:
            w_name = json.dumps(name_remove, ensure_ascii=False)
            w.seek(0)
            w.write(w_name)
        print(shcema_data)
        res_schema_rename = schema.schema_revise(shcema_data)
    print('[res_schema_rename]', res_schema_rename.json())
    return res_schema_rename


# 删除元素，并删除json文件的元素数据
def schema_del():
    schema = Schema()
    path = app.base_dir+'/files/schema_data.json'
    with open(path, 'r+', encoding='utf-8') as w:
        r_data = file_operate.try_open('schema_data')
        if not r_data:
            file_operate.save_data('schema_data', [{'name': '元素1'}])
            r_data = json.loads(w.read())
        while True:
            if len(r_data) < 4:
                schema_add()
                with open(path, 'r+', encoding='utf-8') as r:
                    r_data = json.loads(r.read())
                print('r_data', len(r_data))
            else:
                with open(path, 'r+', encoding='utf-8') as f:
                    data = json.loads(f.read())
                    ran_name = random.choices(data, k=3)
                    list_name_data = []
                    for i in ran_name:
                        list_name_data.append(i['name'])
                    # 删除还剩下的元素名称
                    name_del = [i for i in data if i['name'] not in list_name_data]
                    for name in name_del:
                        name['multi'] = False
                        name['app'] = 129
                    shcema_data = {'appId': '129', 'schema': name_del}
                    a = json.dumps(name_del, indent=8, ensure_ascii=False)
                    f.seek(0)
                    f.truncate()
                    f.write(a)
                    res_schema_del = schema.schema_revise(shcema_data)

                break
        print('[res_schema_del]', res_schema_del.json())
        return res_schema_del


#   移除所有的元素
def schema_remove():
    schema = Schema()
    schema_data = {'appId': '129', 'schema': []}
    res_schema_remove = schema.schema_revise(schema_data)
    print('[res_schema_remove]', res_schema_remove.json())
    return res_schema_remove
