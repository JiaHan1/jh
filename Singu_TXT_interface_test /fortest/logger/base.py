import os
import time
import datetime
from tool.file import write_file


class InstanceInfo:

    def __init__(self):
        self.start_time = time.time()
        self.error_list = list()


class ThisLog:

    def __init__(self):
        self.datadict = dict()
        self.logger_base_dir = os.path.join('data', str(datetime.datetime.now().strftime("%m_%d_%Y_%H:%M:%S")))
        os.mkdir(self.logger_base_dir)

    def start(self, name):
        self.datadict[name]: InstanceInfo = InstanceInfo()
        self.do_log(name, '开始执行')

    def error(self, name, error):
        if name in self.datadict:
            self.datadict[name].error_list.append(error)
        self.do_log(name, '执行错误:' + error)

    def do_log(self, name, msg):
        logfile_path = os.path.join(self.logger_base_dir, name + '.log')
        write_file(logfile_path, '用例:' + name + ',' + msg)

    def create_report(self):
        pass


LOG = ThisLog()
