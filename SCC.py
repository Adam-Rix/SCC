import pytest

from SCC.builder import Ratt

#vers 0.0.1
'''Place here any link which lead u to the error page with text on it "Failed to load API definition.'''
@pytest.mark.parametrize("swagger_url",
                         ["#here#"])
def test_all_requests(driver, swagger_url):

    rat = Ratt(driver)

    rat.open_swagger_page(swagger_url)

    print("Always is fine")