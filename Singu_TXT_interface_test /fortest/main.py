from concurrent.futures.process import ProcessPoolExecutor
from instance.instance import create_instance
from instance.base import BaseInstance
from behavior import STEP_MAP
from logger.base import LOG
from tool.common_func import check_dict_keys, get_random_char
worker_number = 10
executor = ProcessPoolExecutor(worker_number)


if __name__ == '__main__':
    # 生成用例
    instance_dict = create_instance()
    # 执行用例
    for step in instance_dict:
        name_list = list()
        for one_dict in instance_dict[step]:
            if check_dict_keys(one_dict, 'point_list', 'behavior_list'):
                name = get_random_char(5)
                while name in name_list:
                    name = get_random_char(5)
                name_list.append(name)
                BaseInstance(STEP_MAP[step] + '_' + name, one_dict['behavior_list'], one_dict['point_list']).run()
                # executor.submit(one_instance.run())
    # 生成报告
    LOG.create_report()
