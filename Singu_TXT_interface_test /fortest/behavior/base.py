import time
from threading import Thread
from center.request_data import RequestData
from center.object_data import ObjectData


class BaseBehavior:

    Name = '基础行为'

    def __init__(self, request_data: RequestData, object_data: ObjectData):
        self.request_data = request_data
        self.object_data = object_data
        self.api_ok = False

    def run(self):
        Thread(target=self.do_api).start()
        self.local_behavior()
        while not self.api_ok:
            time.sleep(0.2)

    def do_api(self):
        # 执行接口行为
        self.real_do_api()
        self.api_ok = True

    def real_do_api(self):
        # 此方法 用于子类继承
        pass

    def local_behavior(self):
        # 本地推演行为
        pass

    def seed(self):
        # 随机种子生成器
        pass


class PipelineBehavior(BaseBehavior):

    Name = '主线行为'


class OtherBehavior(BaseBehavior):

    Name = '支线行为'
    IS_END = False  # 是否为终止对象
