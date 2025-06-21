def pytest_configure(config):
    config.addinivalue_line("markers", "courses: тесты для работы с курсами")
    config.addinivalue_line("markers", "regression: регрессионные тесты")
    config.addinivalue_line("markers", "smoke: смок тесты")
    config.addinivalue_line("markers", "api: тесты API")
    config.addinivalue_line("markers", "ui: UI-тесты")
    config.addinivalue_line("markers", "critical: критические тесты")
    config.addinivalue_line("markers", "auth: тесты авторизации")
    config.addinivalue_line("markers", "slow: медленные тесты")