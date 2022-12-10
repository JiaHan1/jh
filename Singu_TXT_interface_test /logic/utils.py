from log.log_config import init_log_config


# 判断数据类型是否为列表或元祖
def is_list(lists, list_2):
    list_assert_log = init_log_config('list_assert_log', 'list_assert_log.log')
    data_assert_log = init_log_config('data_assert_log', 'data_assert_log.log')
    if not isinstance(lists, list or tuple):
        try:
            assert lists == list_2, '数据{}的数值校验不通过。期望结果：{}，实际结果：{}'.format(lists, lists, list_2)
        except Exception as e:
            data_assert_log.warning(e)
        return True, True
    for (i, v) in zip(lists, list_2):
        if isinstance(i, list):
            try:
                assert type(v) is list, '数据类型校验不通过。期望结果：list，实际结果：{}'\
                                    .format(type(v))
            except Exception as e_type:
                list_assert_log.warning(e_type)
            is_list(i, v)
            return True, True
        elif isinstance(i, tuple):
            try:
                assert type(v) is tuple, '数据类型校验不通过。期望结果：list，实际结果：{}'\
                                    .format(type(v))
            except Exception as e_type:
                list_assert_log.warning(e_type)
            is_list(i, v)
            return True, True
        elif isinstance(i, dict):
            return i, v
        else:
            try:
                assert i == v, '数值校验不通过。期望结果：{}，实际结果：{}'.format(i, v)
            except Exception as e:
                data_assert_log.warning(e)
            return True, True


# 判断数据类型是否为字典
def is_dict(data_1, data_2):
    dict_key_assert_log = init_log_config('dict_key_assert', 'dict_key_assert.log')
    if isinstance(data_1, dict):
        try:
            assert type(data_2) is dict, '数据{}类型校验不通过。期望类型:字典，实际类型:{}'.format(data_2, type(data_2))
            for i in list(data_2.keys()):
                assert i in list(data_1.keys()), '数据{}字典键值校验不通过。期望结果：{}，实际结果：{}' \
                    .format(data_2, data_1.keys(), i)
        except Exception as e:
            dict_key_assert_log.warning(e)
        dict_values_1 = list(data_1.values())
        dict_values_2 = list(data_2.values())
        for (i, v) in zip(dict_values_1, dict_values_2):
            is_dict(i, v)
            return True, True
    else:
        return data_1, data_2


# 断言数据结构内容
def assert_data(verify_data_1, res_data):
    if isinstance(verify_data_1, dict):
        list1, list2 = is_dict(verify_data_1, res_data)
        print('a', list1, 'b', list2)
        is_list(list1, list2)
    else:
        dict_1, dict_2 = is_list(verify_data_1, res_data)
        is_dict(dict_1, dict_2)
