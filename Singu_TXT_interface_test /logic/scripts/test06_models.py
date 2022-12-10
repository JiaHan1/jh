from api.models import MODEL
from scripts.data_files import dataset_all_files, dataset_training_files
import file_operate
import json
import app


# 创建新模型，直接训练。把返回的的模型训练信息保存到json文件
def model_train():
    model = MODEL()
    with open(app.base_dir+'/files/data_infor.json', 'r+', newline='\n', encoding='utf-8') as w:
        w_data = json.loads(w.read())
        dataset = w_data[0]['id']
        print('dataset', dataset)
    with open(app.base_dir+'/files/training_param.json', 'r+', encoding='utf-8') as r:
        training_param = json.loads(r.read())
        training_param['dataset'] = dataset
        r.seek(0)
        r.truncate()
        r.write(json.dumps(training_param, ensure_ascii=False))
    res_trainingbatch = model.training_batch(training_param)
    if res_trainingbatch.status_code != 200:
        if '数据集中没有训练数据' in res_trainingbatch.json()['message']:
            dataset_all_files()
            dataset_training_files()
        while True:
            res_trainingbatch = model.training_batch(training_param)
            if '模型名称已存在' in res_trainingbatch.json()['message']:
                training_param['name'] = training_param['name'][0:2]+str(int(training_param['name'][2:])+1)
            else:
                file_operate.open_file_w('training_param', training_param)
                break
    else:
        pass
    print('[res_trainingbatch]', res_trainingbatch.json())
    file_operate.save_data('training_batch_id', res_trainingbatch.json())
    res_async_training = model.async_training()
    print(res_async_training.json())
    return res_trainingbatch
