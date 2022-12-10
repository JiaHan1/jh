from point.dataset_about import DatasetFileCorrect, ClassificationAndClusterInDatasetCorrect
from point.file_about import SameNameFileCorrect, ProcessCorrect, FileContentCorrect, DispatchCorrect
from point.label_about import LabelCorrect, LabelMoveCorrect, LabelSchemaCorrect, ClassificationCorrect, ClusterCorrect
from point.model_about import ClusterOverSize, ClassificationOverSize, SchemaInModelCorrect, EvaluateCorrect, \
    PredictCorrect
POINT_MAP = {
    0: {'重名文件是否正确处理': SameNameFileCorrect, '预处理是否正常': PredictCorrect},
    1: {'是否分发给了正确的人': DispatchCorrect},
    2: {'标注内容是否正确': LabelCorrect, '标注迁移是否符合预期': LabelMoveCorrect, '分类是否符合预期': ClassificationCorrect,
        '标注文件的字段是否符合预期': LabelSchemaCorrect},
    3: {'文件的内容是否正确': FileContentCorrect, '标注内容是否正确': LabelCorrect},
    4: {'文件的内容是否正确': FileContentCorrect, '分类是否符合预期': ClassificationCorrect,
        '数据集中文件是否正常': DatasetFileCorrect},
    5: {'标注内容是否正确': LabelCorrect, '模型可选分类是否存在超出训练文件': ClassificationOverSize,
        '模型可选聚类是否存在超出训练文件': ClusterCorrect, '模型中的字段是否正确': SchemaInModelCorrect,
        '数据集中的分类聚类是否正确': ClassificationAndClusterInDatasetCorrect, '模型中的聚类是否异常': ClusterCorrect,
        '模型中的分类是否异常': ClassificationCorrect},
    6: {'评估中的信息是否正常': EvaluateCorrect, '预测的结果是否符合预期': PredictCorrect}
}
