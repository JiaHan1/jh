import requests
import app
import file_operate


class PARSERCONFIG:
    def __init__(self):
        self.url_advance_parser_config = app.BASE_URL + '/api/config/advance_parser_config'
        self.HEADERS = file_operate.extract('token', 'app')

    def advance_parser_config(self, data):
        return requests.post(url=self.url_advance_parser_config, headers=self.HEADERS, data=data, verify=False)

