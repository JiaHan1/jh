from center.request_data import RequestData
from center.object_data import ObjectData
from behavior import BaseBehavior
from logger.base import LOG


class BaseInstance:

    def __init__(self, name, behavior_list: list, point_list: list):
        self.name = name
        self.behavior_list = behavior_list
        self.point_list = point_list
        self.request_data: RequestData = RequestData()
        self.object_data: ObjectData = ObjectData()

    def run(self):
        LOG.start(self.name)
        # 执行用例步骤
        for behavior in self.behavior_list:
            behavior_object: BaseBehavior = behavior(self.request_data, self.object_data)
            behavior_object.run()
        # 获取数据表

        # 执行断言 与断言报告
        # 清理数据
