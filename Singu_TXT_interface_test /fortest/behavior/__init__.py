from behavior.base import BaseBehavior
from behavior.file_step import UploadFileBehavior, ImportFileBehavior, DispatchFileBehavior, \
    UploadSameNameFileBehavior, ReClusterBehavior, DeleteFileBehavior
from behavior.label_step import LabelBehavior, RejectBehavior, ReLabelBehavior, ReClassificationBehavior,\
    ReprocessBehavior, ReDispatchBehavior, ChangeSchemaBehavior, ChangeConfigBehavior, ChangeClassificationBehavior
from behavior.check_step import CheckPassBehavior, CheckRollbackBehavior
from behavior.dataset_step import CreateDatasetBehavior, ChangeTestSetBehavior, ChangeTrainingSetBehavior
from behavior.training_step import TrainingBehavior, DeleteTrainingBatchBehavior
from behavior.predict_step import PredictBehavior, EvaluateBehavior
BEHAVIOR_MAP = {
    'base': BaseBehavior
}

PIPELINE_MAP = {
    0: {'上传文件': UploadFileBehavior, '导入文件': ImportFileBehavior},
    1: {'分发': DispatchFileBehavior},
    2: {'标注': LabelBehavior, '驳回': RejectBehavior},
    3: {'质检通过': CheckPassBehavior, '质检打回': CheckRollbackBehavior},
    4: {'创建数据集': CreateDatasetBehavior},
    5: {'训练': TrainingBehavior},
    6: {'评估': PredictBehavior, '预测': EvaluateBehavior}
}

OTHER_MAP = {
    0: {'导入重名文件': UploadSameNameFileBehavior, '更换聚类模型并重新聚类': ReClusterBehavior,
        '删除文件': DeleteFileBehavior},
    2: {'重新标注': ReLabelBehavior, '重新选分类': ReClassificationBehavior, '重新分发': ReDispatchBehavior,
        '修改字段': ChangeSchemaBehavior, '修改分类': ChangeClassificationBehavior, '修改其他配置': ChangeConfigBehavior,
        '重新预处理': ReprocessBehavior},
    4: {'变更训练集': ChangeTrainingSetBehavior, '变更测试集合': ChangeTestSetBehavior},
    5: {'删除批次模型': DeleteTrainingBatchBehavior}
}

STEP_MAP = {0: '文件', 1: '分发', 2: '标注', 3: '质检', 4: '数据集', 5: '训练', 6: '预测'}
