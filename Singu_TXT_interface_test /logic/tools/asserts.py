from log.log_config import init_log_config


# 公共断言方法
def common_assert(interface_name, res, status_code=400):
    assert_log = init_log_config('common_assert', 'common_assert.log')
    if isinstance(res, list):
        for i_res in res:
            try:
                assert i_res.status_code == status_code, '接口名称{},状态码校验失败，期望值：{}, 实际值：{}' \
                    .format(str(interface_name), status_code, i_res.status_code)
            except Exception as e:
                assert_log.warning(e)
    else:
        try:
            assert res.status_code == status_code, '接口名称{},状态码校验失败，期望值：{}, 实际值：{}'\
                .format(str(interface_name), status_code, res.status_code)
        except Exception as e:
            assert_log.warning(e)


def dict_key_value_assert(json, key_list=None):
    dict_key_value_assert_log = init_log_config('dict_key_value_assert', 'dict_key_value_assert.log')
    if json and key_list is not None:
        json_keys = json.keys()
        for i in json_keys:
            try:
                assert i in key_list, '字典{}中的键{}不存在'.format(json, i)
            except Exception as e:
                dict_key_value_assert_log.warning(e)
    else:
        try:
            assert json == key_list, '字典{}期望结果，为空，断言失败'.format(json)
        except Exception as e_none:
            dict_key_value_assert_log.warning(e_none)


# 数据结构的校验，需要优化
# def data_content_assert(res, data_type_list, layer_num=1, key_list_list=None):
#     data_type_assert_log = init_log_config('data_type_assert', 'data_type_assert.log')
#     res_text = res.text
#     num = 0
#     while True:
#         for i_res in res_text:
#             try:
#                 assert type(res.text) is data_type_list[num], '接口名称{}，从外部{}层类型{},校验失败。实际数据为：{}' \
#                         .format(res, num, data_type_list[num], res.text)
#             except Exception as e:
#                 data_type_assert_log.warning(e)
#             if data_type_list[num] is dict:
#                 dict_key_value_assert(res, key_list_list[num])
#             else:
#                 if num == layer_num:
#                     break


if __name__ == '__main__':
    pass
