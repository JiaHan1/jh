from api.quality_check import Qualitycheck
import file_operate
import json

# 质检文件
def files_to_check():
    quality_check = Qualitycheck()
    res_files_to_check = quality_check.files_to_check()
    print('【res_files_to_check】 ', res_files_to_check.text)
    if res_files_to_check.status_code == 200:
        file_operate.open_file_w('check_files', res_files_to_check.json())
    return res_files_to_check


# 质检通过
def quality_check_pass():
    quality_check = Qualitycheck()
    r_data = file_operate.try_open('check_files')
    if not r_data:
        return True
    res_list = list()
    for i_id in r_data:
        marked_file_id = i_id['marked_file_id']
        data = {"html": "", "check_state": 1, 'marked_file_id': marked_file_id}
        res_quality_check = quality_check.check_file(data)
        print('【res_quality_check】    ', res_quality_check.json())
        res_list.append(res_quality_check)
    return res_list


# 质检不通过
def quality_check_refuse():
    quality_check = Qualitycheck()
    r_data = file_operate.try_open('check_files')
    if not r_data:
        return True
    res_list = list()
    for i_id in r_data:
        marked_file_id = i_id['marked_file_id']
        data = {"html": "", "check_state": 2, 'marked_file_id': marked_file_id}
        res_quality_check = quality_check.check_file(data)
        print('res_quality_check:    ', res_quality_check.json())
        res_list.append(res_quality_check)
    return res_list


if __name__ == "__main__":
    pass
    res = quality_check_pass()
    print(res)
    # quality_check_refuse()