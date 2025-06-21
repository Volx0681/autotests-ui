import pytest

@pytest.mark.slow
def test_slow():
    ...

@pytest.mark.regression
def test_regression():
    ...

@pytest.mark.authorization
def test_authorization():
    ...

@pytest.mark.marking
def test_marking():
    ...