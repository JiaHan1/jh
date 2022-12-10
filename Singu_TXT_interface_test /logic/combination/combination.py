from itertools import combinations
import app
import sys
from log.log_config import init_log_config
from scripts.test10_app import create_app
from scripts.test11_advance_parser_config import advance_parser_config
from scripts.test01_login import login
from scripts.test02_files import upload_file, page_list, dispatch_files
from scripts.test03_label import get_file_content, label
from scripts.test04_quality_check import files_to_check, quality_check_pass, quality_check_refuse
from scripts.test05_datasets import dataset, data_page_list, dataset_all_files, dataset_training_files,\
    dataset_testing_files, dataset_copy
# from scripts.test06_models import model_train
from scripts.test07_inference import inference
from scripts.test08_project_detail import class_add, class_rename, class_del, class_remove
from scripts.test09_schema import schema_add, schema_rename, schema_del, schema_remove
sys.path.append(r"/Users/jiahan/Desktop/TXT_interface/logic")


# 接口逻辑组合，入参为接口列表
def combination(interface):
    log_case = init_log_config('log_case', app.base_dir + '/log/log_file/case.log')
    log_res_error = init_log_config('log_res_error', app.base_dir + '/log/log_file/combination_res_error.log')
    count = -1
    for num in range(len(interface)+1):
        print('接口组合数：', num)
        for i in combinations(interface, num):
            case = []
            count += 1
            errro_infor_list = []
            for func in i:
                error_infor = {}
                name = func.__name__
                case.append(name)
                try:
                    res = func()
                    if isinstance(res, list):
                        for i_res in res:
                            if i_res.status_code != 200:
                                error_infor[str(name)] = str(i_res.json())
                                errro_infor_list.append(error_infor)
                                try:
                                    if isinstance(i_res.json(), dict):
                                        if 'needLogin' in i_res.json().values():
                                            login()
                                except Exception as e_func_error:
                                    raise ValueError(e_func_error)
                    elif isinstance(res, bool):
                        pass
                    else:
                        try:
                            if isinstance(res.json(), dict):
                                if 'needLogin' in res.json().values():
                                    login()
                        except Exception as e_func_error:
                            raise ValueError(e_func_error)
                        if res.status_code == 200:
                            pass
                        else:
                            error_infor[str(name)] = str(res.text)
                            errro_infor_list.append(error_infor)
                except Exception as e_error:
                    raise ValueError('调用{}函数出现问题{}'.format(name, e_error))
            log_case.info('【用例】 {}  {}  '.format(count, case))
            if not errro_infor_list:
                pass
            else:
                log_res_error.error('接口组合用例为{},  接口报错信息为{}'.format(case, errro_infor_list))


func_list = [upload_file, page_list, dispatch_files, get_file_content, label,
             files_to_check, quality_check_pass, quality_check_refuse,
             dataset, data_page_list, dataset_all_files,
             dataset_training_files, dataset_testing_files, dataset_copy, inference,
             class_add, class_rename, class_del, class_remove, schema_add, schema_rename, schema_del, schema_remove]


if __name__ == '__main__':
    combination(func_list)
