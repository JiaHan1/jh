import file_operate
from api.advance_parser_config import PARSERCONFIG


def advance_parser_config():
    advance_parser = PARSERCONFIG()
    data = file_operate.open_file_r('parser_config')
    res_advance_parser = advance_parser.advance_parser_config(data)
    print('【res_advance_parser】', res_advance_parser.text)
    return res_advance_parser


if __name__ == '__main__':
    advance_parser_config()