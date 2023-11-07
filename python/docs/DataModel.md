# DataModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datamodel_links** | [**DatamodelLinks**](DatamodelLinks.md) |  | 
**input** | [**DataModels**](DataModels.md) |  | 
**output** | [**DataModels**](DataModels.md) |  | 

## Example

```python
from datasheets_openapi_client.models.data_model import DataModel

# TODO update the JSON string below
json = "{}"
# create an instance of DataModel from a JSON string
data_model_instance = DataModel.from_json(json)
# print the JSON string representation of the object
print DataModel.to_json()

# convert the object into a dict
data_model_dict = data_model_instance.to_dict()
# create an instance of DataModel from a dict
data_model_form_dict = data_model.from_dict(data_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


