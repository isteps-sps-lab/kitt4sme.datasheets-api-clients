# ModuleProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**management** | [**List[ModuleProperty]**](ModuleProperty.md) |  | [optional] 
**quality** | [**List[ModuleProperty]**](ModuleProperty.md) |  | [optional] 
**operator** | [**List[ModuleProperty]**](ModuleProperty.md) |  | [optional] 
**performance** | [**List[ModuleProperty]**](ModuleProperty.md) |  | [optional] 

## Example

```python
from datasheets_openapi_client.models.module_properties import ModuleProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleProperties from a JSON string
module_properties_instance = ModuleProperties.from_json(json)
# print the JSON string representation of the object
print ModuleProperties.to_json()

# convert the object into a dict
module_properties_dict = module_properties_instance.to_dict()
# create an instance of ModuleProperties from a dict
module_properties_form_dict = module_properties.from_dict(module_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


