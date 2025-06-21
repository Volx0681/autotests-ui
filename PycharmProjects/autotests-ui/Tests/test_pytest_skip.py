import pytest

@pytest.mark.skip(reason="in dev")
def test_feature_in_development():
    ...
class TestSuiteSkip:
    @pytest.mark.skip(reason="in dev")
    def test_feature_in_dev_1(self):
    ...

   def test_feature_in_dev_2(self):
       ...