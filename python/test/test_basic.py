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
import datetime

from datasheets_openapi_client.models.basic import Basic  # noqa: E501

class TestBasic(unittest.TestCase):
    """Basic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Basic:
        """Test Basic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Basic`
        """
        model = Basic()  # noqa: E501
        if include_optional:
            return Basic(
                process = [
                    ''
                    ]
            )
        else:
            return Basic(
        )
        """

    def testBasic(self):
        """Test Basic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
