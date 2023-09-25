import pytest


@pytest.mark.usefixtures("dataload")
class TestExample:
    def test_data(self,dataload):
        print (dataload)

