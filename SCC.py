#vers 0.0.4

import pytest

from SCC.builder import Ratt
from SCC.request_searcher import Searcher


'''Place here any link which lead u to the error page with text on it "Failed to load API definition.'''
@pytest.mark.parametrize("swagger_url",
                         ["*here*"])
def test_all_requests(driver, swagger_url):

    #defining vlues
    rat = Ratt(driver)
    searcher = Searcher(driver)

    #open webpage + open all arrow-tabs
    rat.open_swagger_page(swagger_url)
    rat.open_arrows()

    #collecting requests + body
    searcher.collect_reqsts()
    searcher.collect_body_request()

    #collecting body responses
    searcher.collect_body_response()

    print("\n" + "Always is fine")