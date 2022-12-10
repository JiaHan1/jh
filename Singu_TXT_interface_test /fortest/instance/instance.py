import random
from itertools import combinations
from point import POINT_MAP
from behavior import PIPELINE_MAP, OTHER_MAP
from behavior.base import OtherBehavior
temp_all = dict()


def create_instance() -> dict:
    instance_dict = dict()
    last_step_behavior_group_list = list()
    for step in PIPELINE_MAP:
        instance_list = list()
        step_behavior_group_list = list()
        all_behavior = get_behavior(step)
        for pipeline_name in PIPELINE_MAP[step]:
            for item in all_behavior:
                behavior_list = [PIPELINE_MAP[step][pipeline_name]]
                if item:
                    behavior_list.extend(item)
                if last_step_behavior_group_list:
                    behavior_list = last_step_behavior_group_list[random.randint(
                        0, len(last_step_behavior_group_list) - 1)] + behavior_list
                one_point_list = list()
                if step in POINT_MAP:
                    one_point_list.extend(POINT_MAP[step].values())
                step_behavior_group_list.append(behavior_list)
                instance_list.append({'behavior_list': behavior_list, 'point_list': one_point_list})
        instance_dict[step] = instance_list
        last_step_behavior_group_list = step_behavior_group_list
    return instance_dict


def all_per(can_group_dict):
    temp_list1 = list()
    for i in range(len(can_group_dict) + 1):
        for c in combinations(can_group_dict.keys(), i):  # 其实主要用到的是这个函数
            temp_list1.append(c)
    temp_list2 = list()
    for one_temp in temp_list1:
        small_temp_list = list()
        for name in one_temp:
            behavior: OtherBehavior = can_group_dict[name]
            small_temp_list.append(behavior)
            if behavior.IS_END:
                break
        temp_list2.append(small_temp_list)
    return temp_list2


def get_behavior(out_key):
    if out_key in temp_all:
        return temp_all[out_key]
    can_group_dict = dict()
    for sub_key in OTHER_MAP:
        if out_key >= sub_key:
            can_group_dict.update(OTHER_MAP[sub_key])
    all_behavior = all_per(can_group_dict)
    temp_all[out_key] = all_behavior
    return all_behavior
