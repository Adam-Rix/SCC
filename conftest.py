import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def driver():
    ################## Setup ##################
    options = Options()
    options.add_argument("--incognito")

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()

    ################## Teardown ##################

    yield driver
    driver.quit()