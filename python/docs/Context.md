# Context


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefits** | [**Benefits**](Benefits.md) |  | 
**category** | [**Category**](Category.md) |  | 
**features** | [**Features**](Features.md) |  | 
**productiveaxis** | [**Productiveaxis**](Productiveaxis.md) |  | 
**usecase** | [**Usecase**](Usecase.md) |  | 
**description** | **str** |  | [optional] 
**industry** | **List[str]** |  | [optional] 

## Example

```python
from datasheets_openapi_client.models.context import Context

# TODO update the JSON string below
json = "{}"
# create an instance of Context from a JSON string
context_instance = Context.from_json(json)
# print the JSON string representation of the object
print Context.to_json()

# convert the object into a dict
context_dict = context_instance.to_dict()
# create an instance of Context from a dict
context_form_dict = context.from_dict(context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


