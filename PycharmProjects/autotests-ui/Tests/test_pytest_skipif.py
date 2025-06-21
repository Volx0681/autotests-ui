import pytest

SYSTEM_VERSION = "1.0.0"

@pytest.mark.skipif(SYSTEM_VERSION == "1.3.0", reason="outdated")
def test_system_version_valid():
    ...

@pytest.mark.skipif(SYSTEM_VERSION== 1.0.0, reason="wrong_version")
def test_system_version_invalid():
    ...