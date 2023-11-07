# HardwareDependency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_level** | **str** |  | 
**module_link** | **str** |  | 
**device_text** | **str** |  | [optional] 

## Example

```python
from datasheets_openapi_client.models.hardware_dependency import HardwareDependency

# TODO update the JSON string below
json = "{}"
# create an instance of HardwareDependency from a JSON string
hardware_dependency_instance = HardwareDependency.from_json(json)
# print the JSON string representation of the object
print HardwareDependency.to_json()

# convert the object into a dict
hardware_dependency_dict = hardware_dependency_instance.to_dict()
# create an instance of HardwareDependency from a dict
hardware_dependency_form_dict = hardware_dependency.from_dict(hardware_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


