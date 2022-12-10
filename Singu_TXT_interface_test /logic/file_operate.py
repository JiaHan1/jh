import json
import app


# 保存数据到json文件，更新数据,入参为字典
def save(res):
    bath=app.base_dir+'/files/res.json'
    with open(bath, 'r+', newline='\n', encoding='utf-8') as f_r:
        data=json.loads(f_r.read())

        for key in res.keys():
            value=res[key]
            if 'error_code' not in key and 'message' not in key:
                if key not in data.keys():
                    data[key]=None
                if value != data[key]:

                    data[key]=res[key]


        data_str=json.dumps(data,indent=8,ensure_ascii=False)
        f_r.seek(0)
        f_r.truncate()
        f_r.write(data_str)



# 获取json文件中的数据，入参为字符串
def extract (*data):
    bath = app.base_dir + '/files/res.json'
    with open(bath, 'r+', encoding='utf-8') as f_w:
        data_json={}
        res_json=json.loads(f_w.read())



        for i in data:

            if res_json.get(i) ==None:
                print("未获取到值：",i)

            data_json[i]=str(res_json.get(i))

    return data_json

def extract_value(*data):
    bath = app.base_dir + '/files/res.json'
    with open(bath, 'r+', encoding='utf-8') as f_v:
        res_json = json.loads(f_v.read())

        for i in data:
            if res_json.get(i) == None:
                print("未获取到字典的值：", i)

            value= res_json.get(i)

    return value



def save_data(file,res):
    bath = app.base_dir+'/files/{}.json'
    with open(bath.format(file), 'r+',newline='\n',encoding='utf-8') as f_r:
        # data=json.loads(f_r.read())
        #
        # for key in res.keys():
        #     value=res[key]
        #     if value!=None:
        #
        #         if key not in data.keys():
        #             data[key]=None
        #         if value != data[key]:
        #
        #             data[key]=res[key]
        #
        #
        data_str=json.dumps(res,indent=8,ensure_ascii=False)
        f_r.seek(0)
        f_r.truncate()
        f_r.write(data_str)



# 获取json文件中的数据，入参为提取的文件名，字符串
def extract_data (file,*data):
    bath = app.base_dir + '/files/{}.json'
    with open(bath.format(file), 'r+', encoding='utf-8') as f_w:
        data_json={}
        res_json=json.loads(f_w.read())
        try:

            for i in data:
                if res_json.get(i) ==None:
                    print("未获取到值：",i)

                data_json[i]=res_json.get(i)

        except:
            for i_res in res_json:
                for i_data in data:
                    # 此为文件为字典格式
                    try:
                        if i_data in i_res.keys():
                            if i_res[i_data]==None:
                                print("未获取到值：", i_data)
                            else:
                                data_json[i_data] = i_res[i_data]
                    # 此为非字典格式
                    except:
                        data_list=[]
                        if i_data == i_res:
                            data_list.append(i_data)
                            return data_list
    return data_json


def open_file_r(file):
    path = app.base_dir + '/files/{}.json'
    with open(path.format(file), 'r+', encoding='utf-8') as f_r:
        data = json.loads(f_r.read())
        return data


def open_file_w(file, data):
    path = app.base_dir + '/files/{}.json'
    with open(path.format(file), 'r+', encoding='utf-8') as f_w:
        data_str = json.dumps(data, indent=8, ensure_ascii=False)
        f_w.seek(0)
        f_w.truncate()
        f_w.write(data_str)


def try_open(file_name):
    data = []
    try:
        data = open_file_r(str(file_name))
    except Exception as e:
        print(' class_add 无内容', e)
        data = []
    finally:
        return data
