#vers 0.0.2

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

    rat.open_swagger_page(swagger_url)

    searcher.collect_reqsts()

    print("\n" + "Always is fine")