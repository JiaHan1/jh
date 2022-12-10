import json
import datetime


def write_file(path, content, is_append=True):
    with open(path, 'a' if is_append else 'w', encoding='utf-8') as file_handler:
        if type(content) != str:
            content = json.dumps(content, ensure_ascii=False, indent=4)
        content = str(datetime.datetime.now()) + ':' + content
        file_handler.write(content)
