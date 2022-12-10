from point.base import BasePoint


class SameNameFileCorrect(BasePoint):

    NAME = '重名文件是否正确处理'


class ProcessCorrect(BasePoint):

    NAME = '预处理是否正常'


class FileContentCorrect(BasePoint):

    NAME = '文件的内容是否正确'


class DispatchCorrect(BasePoint):

    NAME = '是否分发给了正确的人'
