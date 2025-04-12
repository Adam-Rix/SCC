#version 0.1.0

import pytest

from SCC.builder import Ratt
from SCC.request_searcher import Searcher
from SCC.request_sender import Sender

'''Place here any link which lead u to the error page with text on it "Failed to load API definition.'''
@pytest.mark.parametrize("swagger_url",
                         ["*swagger_url_here*"]) # take this from env in the nearest future
def test_all_requests(driver, swagger_url):

    # defining vlues
    rat = Ratt(driver)
    searcher = Searcher(driver)
    send = Sender(driver)

    # open webpage + open all arrow-tabs
    rat.open_swagger_page(swagger_url)
    rat.open_arrows()

    # collecting requests + body
    searcher.collect_request()
    searcher.collect_body_request()
    # requests = searcher.collect_request() ## switch on that when sending_collected_requests will be done
    # bodies = searcher.collect_body_request() ## switch on that when sending_collected_requests will be done

    # collecting body responses
    searcher.collect_body_response()

    # # sending collected_requests from swagger page for v0.0.6
    # send.request_former(
    #     requests_list=requests,
    #     body_requests_list=bodies,
    #     base_url="*base_url_here*" # take this from env in the nearest future
    # )
    #
    # # correlation of collected and received responses for v0.1.0
    # send.request_correlator()

    # erase or change this print beneath for v1.0.0
    print("\n" + "Always is fine")