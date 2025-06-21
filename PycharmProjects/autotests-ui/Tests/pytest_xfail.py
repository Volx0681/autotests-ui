import pytest

@pytest.mark.xfail(reason="найден баг с падением в ошибку")
def test_with_bug():
        assert 1 == 2

@pytest.mark.xfail(reason="баг исправлен но надо проверить")
def test_without_bug():
    ...