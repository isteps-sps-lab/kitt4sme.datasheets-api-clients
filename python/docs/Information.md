# Information


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_accronym** | **str** |  | 
**component_name** | **str** |  | 
**component_uuid** | **str** |  | 
**provider** | **str** |  | 
**version** | **str** |  | [optional] 

## Example

```python
from datasheets_openapi_client.models.information import Information

# TODO update the JSON string below
json = "{}"
# create an instance of Information from a JSON string
information_instance = Information.from_json(json)
# print the JSON string representation of the object
print Information.to_json()

# convert the object into a dict
information_dict = information_instance.to_dict()
# create an instance of Information from a dict
information_form_dict = information.from_dict(information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


