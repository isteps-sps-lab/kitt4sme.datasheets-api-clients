# Datasheet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**Context**](Context.md) |  | 
**datamodel** | [**DataModel**](DataModel.md) |  | 
**information** | [**Information**](Information.md) |  | 
**keycloak_id** | **str** |  | 
**module_properties** | [**ModuleProperties**](ModuleProperties.md) |  | 
**public_endpoints** | [**PublicEndpoints**](PublicEndpoints.md) |  | 
**skills** | [**Skills**](Skills.md) |  | 
**support** | [**Support**](Support.md) |  | 
**technicalrequirements** | [**TechnicalRequirements**](TechnicalRequirements.md) |  | 
**datasheet_id** | **int** |  | [optional] 
**hardware_dependencies** | [**List[HardwareDependency]**](HardwareDependency.md) |  | [optional] 
**software_dependencies** | [**List[SoftwareDependency]**](SoftwareDependency.md) |  | [optional] 

## Example

```python
from datasheets_openapi_client.models.datasheet import Datasheet

# TODO update the JSON string below
json = "{}"
# create an instance of Datasheet from a JSON string
datasheet_instance = Datasheet.from_json(json)
# print the JSON string representation of the object
print Datasheet.to_json()

# convert the object into a dict
datasheet_dict = datasheet_instance.to_dict()
# create an instance of Datasheet from a dict
datasheet_form_dict = datasheet.from_dict(datasheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


