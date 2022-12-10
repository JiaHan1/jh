import json


def load_json(json_str):
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return None
    else:
        return data


def check_dict_keys(my_dict, *args):
    if type(my_dict) == dict:
        for one_key in args:
            if one_key in my_dict:
                continue
            else:
                return False
        return True
    return False
