# #vers 0.0.3

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Searcher:
    def __init__(self, driver):
        self.driver = driver

    def collect_reqsts(self):

        method_elements = self.driver.find_elements(By.CLASS_NAME,
                                               "opblock-summary-method")

        requests_list = []

        for method_element in method_elements:

            request_type = method_element.text.strip().upper()

            parent_element = method_element.find_element(By.XPATH,
                                                         "./ancestor::div[contains(@class, 'opblock-tag-section is-open')]")
            api_path_element = parent_element.find_element(By.CLASS_NAME,
                                                           "opblock-summary-path")
            api_path = api_path_element.text.strip()

            requests_list.append({
                "method": request_type,
                "path": api_path
            })

        print(f"~Total API requests found: {len(requests_list)}" + "\n")
        for req in requests_list:
            print(f"{req['method']} - {req['path']}")