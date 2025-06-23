pytest_plugins = ("fixtures.browsers",)

import sys
sys.path.insert(0, "C:/Users/silen/PycharmProjects/autotests-ui")

def pytest_configure(config):

    markers = [
        "courses: тесты для работы с курсами",
        "regression: регрессионные тесты",
        "smoke: смок тесты",
        "api: тесты API",
        "ui: UI-тесты",
        "critical: критические тесты",
        "auth: тесты авторизации",
        "slow: медленные тесты"
    ]

    for marker in markers:
        config.addinivalue_line("markers", marker)