# coding: utf-8

"""
    Datasheets Backend

    This is Datasheet backend API documentation. This is intended only for development purposes

    The version of the OpenAPI document: 1.0.1
    Contact: kari.kolehmainen@vtt.fi
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from datasheets_openapi_client.api.datasheets_api import DatasheetsApi  # noqa: E501


class TestDatasheetsApi(unittest.TestCase):
    """DatasheetsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DatasheetsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_datasheets_get(self) -> None:
        """Test case for datasheets_get

        Returns validated datasheets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()