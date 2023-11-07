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

from datasheets_openapi_client.models.api_response import ApiResponse  # noqa: E501

class TestApiResponse(unittest.TestCase):
    """ApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiResponse:
        """Test ApiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiResponse`
        """
        model = ApiResponse()  # noqa: E501
        if include_optional:
            return ApiResponse(
                data = [
                    datasheets_openapi_client.models.datasheet.Datasheet(
                        context = datasheets_openapi_client.models.context.Context(
                            benefits = datasheets_openapi_client.models.benefits.Benefits(
                                operator = datasheets_openapi_client.models.benefit3_fields.Benefit3Fields(
                                    1 = True, 
                                    2 = True, 
                                    3 = True, ), 
                                production = datasheets_openapi_client.models.benefit2_fields.Benefit2Fields(
                                    1 = True, 
                                    2 = True, ), 
                                quality = datasheets_openapi_client.models.benefit2_fields.Benefit2Fields(
                                    1 = True, 
                                    2 = True, ), 
                                machine = , ), 
                            category = datasheets_openapi_client.models.category.Category(
                                decisionmaker = True, 
                                reasoning = True, ), 
                            features = datasheets_openapi_client.models.features.Features(
                                management = [
                                    ''
                                    ], 
                                performance = [
                                    ''
                                    ], ), 
                            productiveaxis = datasheets_openapi_client.models.productiveaxis.Productiveaxis(
                                ai_hri = True, 
                                ai_manualactivity = True, 
                                ai_quality = True, ), 
                            usecase = datasheets_openapi_client.models.usecase.Usecase(
                                usecasedesc = '', ), 
                            description = '', 
                            industry = [
                                ''
                                ], ), 
                        datamodel = datasheets_openapi_client.models.data_model.DataModel(
                            datamodel_links = datasheets_openapi_client.models.datamodel_links.DatamodelLinks(
                                input = '', 
                                output = '', ), 
                            input = datasheets_openapi_client.models.data_models.DataModels(
                                devices = [
                                    ''
                                    ], 
                                factory = [
                                    ''
                                    ], 
                                measurements = [
                                    ''
                                    ], 
                                workers = [
                                    ''
                                    ], ), 
                            output = datasheets_openapi_client.models.data_models.DataModels(), ), 
                        information = datasheets_openapi_client.models.information.Information(
                            component_accronym = '', 
                            component_name = '', 
                            component_uuid = '', 
                            provider = '', 
                            version = '', ), 
                        keycloak_id = '', 
                        module_properties = datasheets_openapi_client.models.module_properties.ModuleProperties(), 
                        public_endpoints = datasheets_openapi_client.models.public_endpoints.PublicEndpoints(
                            oapi = True, ), 
                        skills = datasheets_openapi_client.models.skills.Skills(
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
                                    ], ), ), 
                        support = datasheets_openapi_client.models.support.Support(
                            online_resources = '', ), 
                        technicalrequirements = datasheets_openapi_client.models.technical_requirements.TechnicalRequirements(
                            disk_unit = '', 
                            gpu_unit = '', 
                            multienancy_support = datasheets_openapi_client.models.requirement_support.RequirementSupport(
                                checkbox = True, ), 
                            multiuser_support = datasheets_openapi_client.models.requirement_support.RequirementSupport(
                                checkbox = True, ), 
                            ram_unit = '', 
                            dashboard = '', 
                            os = [
                                ''
                                ], 
                            protocol = [
                                datasheets_openapi_client.models.protocol_item.ProtocolItem(
                                    name = '', )
                                ], 
                            requirement_cpu = '', 
                            requirement_disk = '', 
                            requirement_gpu = '', 
                            requirement_ram = '', ), 
                        datasheet_id = 56, 
                        hardware_dependencies = [
                            datasheets_openapi_client.models.hardware_dependency.HardwareDependency(
                                dependency_level = '', 
                                device_link = '', 
                                device_text = '', )
                            ], 
                        software_dependencies = [
                            datasheets_openapi_client.models.software_dependency.SoftwareDependency(
                                dependency_level = '', 
                                module_link = '', 
                                module_text = '', 
                                module_version = '', 
                                module_id = '', )
                            ], )
                    ],
                message = '',
                status_code = 56
            )
        else:
            return ApiResponse(
                data = [
                    datasheets_openapi_client.models.datasheet.Datasheet(
                        context = datasheets_openapi_client.models.context.Context(
                            benefits = datasheets_openapi_client.models.benefits.Benefits(
                                operator = datasheets_openapi_client.models.benefit3_fields.Benefit3Fields(
                                    1 = True, 
                                    2 = True, 
                                    3 = True, ), 
                                production = datasheets_openapi_client.models.benefit2_fields.Benefit2Fields(
                                    1 = True, 
                                    2 = True, ), 
                                quality = datasheets_openapi_client.models.benefit2_fields.Benefit2Fields(
                                    1 = True, 
                                    2 = True, ), 
                                machine = , ), 
                            category = datasheets_openapi_client.models.category.Category(
                                decisionmaker = True, 
                                reasoning = True, ), 
                            features = datasheets_openapi_client.models.features.Features(
                                management = [
                                    ''
                                    ], 
                                performance = [
                                    ''
                                    ], ), 
                            productiveaxis = datasheets_openapi_client.models.productiveaxis.Productiveaxis(
                                ai_hri = True, 
                                ai_manualactivity = True, 
                                ai_quality = True, ), 
                            usecase = datasheets_openapi_client.models.usecase.Usecase(
                                usecasedesc = '', ), 
                            description = '', 
                            industry = [
                                ''
                                ], ), 
                        datamodel = datasheets_openapi_client.models.data_model.DataModel(
                            datamodel_links = datasheets_openapi_client.models.datamodel_links.DatamodelLinks(
                                input = '', 
                                output = '', ), 
                            input = datasheets_openapi_client.models.data_models.DataModels(
                                devices = [
                                    ''
                                    ], 
                                factory = [
                                    ''
                                    ], 
                                measurements = [
                                    ''
                                    ], 
                                workers = [
                                    ''
                                    ], ), 
                            output = datasheets_openapi_client.models.data_models.DataModels(), ), 
                        information = datasheets_openapi_client.models.information.Information(
                            component_accronym = '', 
                            component_name = '', 
                            component_uuid = '', 
                            provider = '', 
                            version = '', ), 
                        keycloak_id = '', 
                        module_properties = datasheets_openapi_client.models.module_properties.ModuleProperties(), 
                        public_endpoints = datasheets_openapi_client.models.public_endpoints.PublicEndpoints(
                            oapi = True, ), 
                        skills = datasheets_openapi_client.models.skills.Skills(
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
                                    ], ), ), 
                        support = datasheets_openapi_client.models.support.Support(
                            online_resources = '', ), 
                        technicalrequirements = datasheets_openapi_client.models.technical_requirements.TechnicalRequirements(
                            disk_unit = '', 
                            gpu_unit = '', 
                            multienancy_support = datasheets_openapi_client.models.requirement_support.RequirementSupport(
                                checkbox = True, ), 
                            multiuser_support = datasheets_openapi_client.models.requirement_support.RequirementSupport(
                                checkbox = True, ), 
                            ram_unit = '', 
                            dashboard = '', 
                            os = [
                                ''
                                ], 
                            protocol = [
                                datasheets_openapi_client.models.protocol_item.ProtocolItem(
                                    name = '', )
                                ], 
                            requirement_cpu = '', 
                            requirement_disk = '', 
                            requirement_gpu = '', 
                            requirement_ram = '', ), 
                        datasheet_id = 56, 
                        hardware_dependencies = [
                            datasheets_openapi_client.models.hardware_dependency.HardwareDependency(
                                dependency_level = '', 
                                device_link = '', 
                                device_text = '', )
                            ], 
                        software_dependencies = [
                            datasheets_openapi_client.models.software_dependency.SoftwareDependency(
                                dependency_level = '', 
                                module_link = '', 
                                module_text = '', 
                                module_version = '', 
                                module_id = '', )
                            ], )
                    ],
                message = '',
                status_code = 56,
        )
        """

    def testApiResponse(self):
        """Test ApiResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
