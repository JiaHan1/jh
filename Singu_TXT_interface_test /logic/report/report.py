import pytest
class TestClass:
    def test01(self):
        res_001 = 1
        assert res_001==1

    def test02(self):
        res_002 = 1
        assert res_002 == 1

if __name__ == '__main__':
    pytest.main(['-v', '--html=./Singu_TXT_interface.html', '--self-contained-html','report.py'])