import os
import yaml
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#vers 0.0.1
@pytest.fixture(scope='session')
def driver():
    ################## Setup ##################
    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    ################## Teardown ##################

    yield driver
    driver.quit()