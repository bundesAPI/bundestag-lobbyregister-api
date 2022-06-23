"""
    Bundestag: Lobbyregister API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.bundestag_lobbyregister.model.activity import Activity
from deutschland.bundestag_lobbyregister.model.client_organization import (
    ClientOrganization,
)
from deutschland.bundestag_lobbyregister.model.donator import Donator
from deutschland.bundestag_lobbyregister.model.entry_account import EntryAccount
from deutschland.bundestag_lobbyregister.model.entry_employee_count import (
    EntryEmployeeCount,
)
from deutschland.bundestag_lobbyregister.model.entry_financial_expenses_euro import (
    EntryFinancialExpensesEuro,
)
from deutschland.bundestag_lobbyregister.model.field_of_interest import FieldOfInterest
from deutschland.bundestag_lobbyregister.model.legislative_project import (
    LegislativeProject,
)
from deutschland.bundestag_lobbyregister.model.lobbyist_identity import LobbyistIdentity
from deutschland.bundestag_lobbyregister.model.media import Media
from deutschland.bundestag_lobbyregister.model.named_employee import NamedEmployee

from deutschland import bundestag_lobbyregister

globals()["Activity"] = Activity
globals()["ClientOrganization"] = ClientOrganization
globals()["Donator"] = Donator
globals()["EntryAccount"] = EntryAccount
globals()["EntryEmployeeCount"] = EntryEmployeeCount
globals()["EntryFinancialExpensesEuro"] = EntryFinancialExpensesEuro
globals()["FieldOfInterest"] = FieldOfInterest
globals()["LegislativeProject"] = LegislativeProject
globals()["LobbyistIdentity"] = LobbyistIdentity
globals()["Media"] = Media
globals()["NamedEmployee"] = NamedEmployee
from deutschland.bundestag_lobbyregister.model.entry import Entry


class TestEntry(unittest.TestCase):
    """Entry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEntry(self):
        """Test Entry"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Entry()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
