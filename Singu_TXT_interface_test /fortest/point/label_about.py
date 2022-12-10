from point.base import BasePoint


class LabelCorrect(BasePoint):

    NAME = '标注文件的内容是否正确'


class LabelMoveCorrect(BasePoint):

    NAME = '标注迁移是否符合预期'


class ClassificationCorrect(BasePoint):
    NAME = '分类是否符合预期'


class LabelSchemaCorrect(BasePoint):
    NAME = '标注文件的字段是否符合预期'


class ClusterCorrect(BasePoint):
    NAME = '聚类是否符合预期'
