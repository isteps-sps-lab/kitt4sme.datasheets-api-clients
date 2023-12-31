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

from datasheets_openapi_client.models.skills import Skills  # noqa: E501

class TestSkills(unittest.TestCase):
    """Skills unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Skills:
        """Test Skills
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Skills`
        """
        model = Skills()  # noqa: E501
        if include_optional:
            return Skills(
                basic = datasheets_openapi_client.models.basic.Basic(
                    process = [
                        ''
                        ], ),
                crossfunctional = datasheets_openapi_client.models.cross_functional.CrossFunctional(
                    problemsolving = [
                        ''
                        ], 
                    social = [
                        ''
                        ], 
                    system = [
                        ''
                        ], 
                    technical = [
                        ''
                        ], )
            )
        else:
            return Skills(
                basic = datasheets_openapi_client.models.basic.Basic(
                    process = [
                        ''
                        ], ),
                crossfunctional = datasheets_openapi_client.models.cross_functional.CrossFunctional(
                    problemsolving = [
                        ''
                        ], 
                    social = [
                        ''
                        ], 
                    system = [
                        ''
                        ], 
                    technical = [
                        ''
                        ], ),
        )
        """

    def testSkills(self):
        """Test Skills"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
