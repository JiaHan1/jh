from api.application import APP
import file_operate


# 创建新的应用，把应用id写入json文件
def create_app():
    app = APP()
    data = {"app_name": "接口测试1", "app_en_name": "", "app_type": 1, "desc": "", "schema": [], "model_id": None}
    while True:
        res_create_app = app.application(data)
        if res_create_app.status_code != 200:
            if '应用名已存在，请查检' in res_create_app.json().values():
                num = data['app_name'][4:]
                num = int(num) + 1
                data['app_name'] = '接口测试'+str(num)
        else:
            print('【res_create_app】', res_create_app.json())
            w_data = {'app': res_create_app.json()['id']}
            print(w_data)
            file_operate.save(w_data)
            break

    return res_create_app


if __name__ == '__main__':
    create_app()
