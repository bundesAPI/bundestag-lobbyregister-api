"""
    Bundestag: Lobbyregister API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.bundestag_lobbyregister.model.entry import Entry

from deutschland import bundestag_lobbyregister

globals()["Entry"] = Entry
from deutschland.bundestag_lobbyregister.model.search_result import SearchResult


class TestSearchResult(unittest.TestCase):
    """SearchResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchResult(self):
        """Test SearchResult"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchResult()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
