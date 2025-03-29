#vers 0.0.3

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#vers 0.0.1
class Ratt:
    def __init__(self,  driver):
        self.driver = driver

    def open_swagger_page(self,
                           url):
        """Open swagger page"""
        self.driver.get(url)

        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, "body"),  # Search in the entire page body
                "Schemas"
            )
        )

        print("\n \n" + "~Requests found: " + "\n")