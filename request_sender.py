#version 0.0.2
import requests
import json

class Sender:
    def __init__(self, driver):
        self.driver = driver
        self.responses_from_server = []

    def request_former(self,
                       requests_list,
                       body_requests_list,
                       base_url):

        for idx, api in enumerate(requests_list):
            method = api["method"].upper()
            path = api["path"]

            if "{hotelId}" in path:
                path = path.replace("{hotelId}", "3701")

            url_request_our = base_url.rstrip("/") + path

            #taking body response if it exists in array
            json_body = None
            if idx < len(body_requests_list):
                try:
                    json_body = json.loads(body_requests_list[idx]["body_request"])
                except json.JSONDecodeError:
                    print(f"⚠️ Невозможно декодировать JSON для {method} or {path}")

            #sending request
            try:
                response = requests.request(method,
                                            url_request_our,
                                            json=json_body)
                print(f"✅ {method} {url_request_our} -> {response.status_code}")

                self.responses_from_server.append({
                    "method": method,
                    "url": url_request_our,
                    "status": response.status_code,
                    "response_body": response.text
                })
            except Exception as e:
                print(f"❌ Ошибка при запросе {method} {url_request_our}: {e}")

    def request_correlator(self):
        pass