import pytest
import sys
from tools.asserts import common_assert
from scripts.test10_app import create_app
from scripts.test11_advance_parser_config import advance_parser_config
from scripts.test02_files import upload_file, page_list, dispatch_files
from scripts.test03_label import get_file_content, label
from scripts.test04_quality_check import files_to_check, quality_check_pass, quality_check_refuse
from scripts.test05_datasets import dataset, data_page_list, dataset_all_files, dataset_training_files,\
    dataset_testing_files, dataset_copy
from scripts.test08_project_detail import class_add, class_rename, class_del, class_remove
from scripts.test09_schema import schema_add, schema_rename, schema_del, schema_remove
sys.path.append(r"/Users/jiahan/Desktop/TXT_interface/logic")


@pytest.mark.usefixtures("init")
class TestClass:
    def test000(self):
        res_create_app = create_app()
        common_assert('create_app', res_create_app)

    def test_advance_parser_config(self):
        res_advance_parser_config = advance_parser_config()
        common_assert('res_advance_parser_config', res_advance_parser_config)

    def test_upload_file(self):
        res_upload_file = upload_file()
        common_assert('upload_file',res_upload_file)

    def test_page_list(self):
        res_page_list = page_list()
        common_assert('page_list', res_page_list)

    def test_dispatch_files(self):
        res_dispatch_files = dispatch_files()
        common_assert('dispatch_files', res_dispatch_files)

    def test_get_file_content(self):
        res_get_file_content = get_file_content()
        common_assert('get_file_content', res_get_file_content)

    def test_label(self):
        res_label = label()
        common_assert('label', res_label)

    def test_files_to_check(self):
        res_files_to_check = files_to_check()
        common_assert('files_to_check', res_files_to_check)

    def test_case007(self):
        res_quality_check_pass = quality_check_pass()
        common_assert('quality_check_pass', res_quality_check_pass)

    def test_quality_check_refuse(self):
        res_quality_check_refuse = quality_check_refuse()
        common_assert('quality_check_refuse', res_quality_check_refuse)

    def test_dataset(self):
        res_dataset = dataset()
        common_assert('dataset', res_dataset)

    def test_data_page_list(self):
        res_data_page_list = data_page_list()
        common_assert('data_page_list', res_data_page_list)

    def test_case011(self):
        res_dataset_all_files = dataset_all_files()
        common_assert('dataset_all_files', res_dataset_all_files)

    def test_dataset_training_files(self):
        res_dataset_training_files = dataset_training_files()
        common_assert('dataset_training_files', res_dataset_training_files)

    def test_dataset_testing_files(self):
        res_dataset_testing_files = dataset_testing_files()
        common_assert('dataset_testing_files', res_dataset_testing_files)

    def test_dataset_copy(self):
        res_dataset_copy = dataset_copy()
        common_assert('dataset_copy' ,res_dataset_copy)

    def test_class_add(self):
        res_class_add = class_add()
        common_assert('class_add', res_class_add)

    def test_class_rename(self):
        res_class_rename= class_rename()
        common_assert('class_rename', res_class_rename)

    def test_class_del(self):
        res_class_del = class_del()
        common_assert('class_del', res_class_del)

    def test_class_remove(self):
        res_class_remove = class_remove()
        common_assert('class_remove', res_class_remove)

    def test_schema_add(self):
        res_schema_add = schema_add()
        common_assert('schema_add', res_schema_add)

    def test_schema_rename(self):
        res_schema_rename = schema_rename()
        common_assert('schema_rename', res_schema_rename)

    def test_schema_del(self):
        res_schema_del = schema_del()
        common_assert('schema_del', res_schema_del)

    def test_schema_remove(self):
        res_schema_remove = schema_remove()
        common_assert('schema_remove', res_schema_remove)


if __name__ == '__main__':
    pass
