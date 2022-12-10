import random
from collections import OrderedDict


def check_dict_keys(one_dict, *args):
    """
    验证字典中键的完备性
    """
    if type(one_dict) == dict or isinstance(one_dict, OrderedDict):
        for field in args:
            if field not in one_dict:
                return False
        return True
    return False


def get_random_char(length=4):
    all_char = '0123456789qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP'
    index = len(all_char) - 1
    result = ''
    for _ in range(length):
        n = random.randint(0, index)
        result += all_char[n]
    return result
