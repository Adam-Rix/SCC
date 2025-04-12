#version 0.1.2

from selenium.webdriver.common.by import By

class Searcher:
    def __init__(self, driver):
        self.driver = driver

    def collect_request(self):

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

        return requests_list

    def collect_body_request(self):

        body_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                  "pre.body-param__example.microlight")

        body_requests_list = []

        for body_element in body_elements:

            body_content = body_element.text.strip()

            body_requests_list.append({
                "body_request": body_content
            })

        print("\n" + f"~~Total examples of body requests found: {len(body_requests_list)}" + "\n")
        for bod in body_requests_list:
            print(f"{bod['body_request']},")

        return body_requests_list

    def collect_body_response(self):

        body_response_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                  "pre.example.microlight")

        codes_table_rows = self.driver.find_elements(
            By.CSS_SELECTOR,
            "table.responses-table > tbody > tr"
        )

        body_responses_list = [] # for json-responses
        response_codes_list = [] # for codes

        for body_response_element in body_response_elements:
            try:
                body_responses_content = body_response_element.text.strip()

                body_responses_list.append({
                    "body_response": body_responses_content
                })

            except Exception as e:

                print(f"⚠️ Alert: Wrong row for collecting {e}")
                continue

        for row in codes_table_rows:
            try:
                code = row.find_element(
                    By.CLASS_NAME,
                    "response-col_status"
                ).text.strip()

                description = row.find_element(
                    By.CSS_SELECTOR,
                    ".response-col_description .renderedMarkdown p"
                ).text.strip()

                response_codes_list.append({
                    "code": code,
                    "description": description
                })

            except Exception as e:

                print(f"⚠️ Alert: Wrong row for collecting {e}")
                continue

        print("\n" + f"~~Total examples of body responses found: {len(body_responses_list)}" + "\n")
        for bod in body_responses_list:
            print(f"{bod['body_response']},")

        print("\n" + f"~~Total response codes found:{len(response_codes_list)}" + "\n")
        for item in response_codes_list:
            print(f"{item['code']} — {item['description']},")

        return body_responses_list, response_codes_list