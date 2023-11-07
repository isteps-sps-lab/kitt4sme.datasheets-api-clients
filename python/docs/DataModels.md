# DataModels


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datamodel** | **List[str]** |  | [optional] 
**devices** | **List[str]** |  | [optional] 
**factory** | **List[str]** |  | [optional] 
**measurements** | **List[str]** |  | [optional] 
**workers** | **List[str]** |  | [optional] 

## Example

```python
from datasheets_openapi_client.models.data_models import DataModels

# TODO update the JSON string below
json = "{}"
# create an instance of DataModels from a JSON string
data_models_instance = DataModels.from_json(json)
# print the JSON string representation of the object
print DataModels.to_json()

# convert the object into a dict
data_models_dict = data_models_instance.to_dict()
# create an instance of DataModels from a dict
data_models_form_dict = data_models.from_dict(data_models_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


