# SoftwareDependency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_level** | **str** |  | 
**module_link** | **str** |  | 
**module_text** | **str** |  | [optional] 
**module_version** | **str** |  | [optional] 
**module_id** | **str** |  | [optional] 

## Example

```python
from datasheets_openapi_client.models.software_dependency import SoftwareDependency

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareDependency from a JSON string
software_dependency_instance = SoftwareDependency.from_json(json)
# print the JSON string representation of the object
print SoftwareDependency.to_json()

# convert the object into a dict
software_dependency_dict = software_dependency_instance.to_dict()
# create an instance of SoftwareDependency from a dict
software_dependency_form_dict = software_dependency.from_dict(software_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


