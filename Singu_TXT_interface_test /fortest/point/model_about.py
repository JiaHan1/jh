from point.base import BasePoint


class ClassificationOverSize(BasePoint):
    NAME = '模型可选分类是否超出'


class ClusterOverSize(BasePoint):
    NAME = '模型可选聚类是否超出'


class SchemaInModelCorrect(BasePoint):
    NAME = '模型中字段是否正常'


class EvaluateCorrect(BasePoint):
    NAME = '评估是否正常'


class PredictCorrect(BasePoint):
    NAME = '预测是否正常'
