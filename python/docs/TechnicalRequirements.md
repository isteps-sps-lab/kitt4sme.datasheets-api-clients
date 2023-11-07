# TechnicalRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_unit** | **str** |  | 
**gpu_unit** | **str** |  | 
**multienancy_support** | [**RequirementSupport**](RequirementSupport.md) |  | 
**multiuser_support** | [**RequirementSupport**](RequirementSupport.md) |  | 
**ram_unit** | **str** |  | 
**dashboard** | **str** |  | [optional] 
**os** | **List[str]** |  | [optional] 
**protocol** | [**List[ProtocolItem]**](ProtocolItem.md) |  | [optional] 
**requirement_cpu** | **str** |  | [optional] 
**requirement_disk** | **str** |  | [optional] 
**requirement_gpu** | **str** |  | [optional] 
**requirement_ram** | **str** |  | [optional] 

## Example

```python
from datasheets_openapi_client.models.technical_requirements import TechnicalRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of TechnicalRequirements from a JSON string
technical_requirements_instance = TechnicalRequirements.from_json(json)
# print the JSON string representation of the object
print TechnicalRequirements.to_json()

# convert the object into a dict
technical_requirements_dict = technical_requirements_instance.to_dict()
# create an instance of TechnicalRequirements from a dict
technical_requirements_form_dict = technical_requirements.from_dict(technical_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


