import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome

from datetime import datetime

from dotenv import load_dotenv

from .data.preset_data import PresetData

load_dotenv()


@pytest.fixture(scope='function')
def browser(request):
    browser = None
    options_chrome = OptionsChrome()
    options_chrome.add_argument('--start-maximized')
    browser = webdriver.Chrome(options=options_chrome)
    yield browser
    browser.quit()


# @pytest.fixture(scope='session', autouse=True)
# def stop_test_if_env_variables_are_empty(request):
#     required_env_variables = [
#         'BASE_URL',
#         'GOSUSLUGI_PASSWORD'
#     ]
#     missing_variables = [var for var in required_env_variables if not os.getenv(var)]
#     if missing_variables:
#         assert False, \
#             f'\nСледующие обязательные переменные окружения не заданы: {", ".join(missing_variables)}' \
#             '\nВсе тесты остановлены.' \
#             '\nЗадайте переменные окружения в файле .env в виде:' \
#             f'\n{missing_variables[0]}=значение'


def pytest_collection_modifyitems(items):
    items[:] = sorted(
        items, key=lambda x: x.get_closest_marker("order").args[0] if x.get_closest_marker("order") else 0)