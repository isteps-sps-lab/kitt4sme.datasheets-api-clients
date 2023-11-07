# Benefits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**macmuhine** | [**Benefit2Fields**](Benefit2Fields.md) |  | [optional] 
**operator** | [**Benefit3Fields**](Benefit3Fields.md) |  | 
**production** | [**Benefit2Fields**](Benefit2Fields.md) |  | 
**quality** | [**Benefit2Fields**](Benefit2Fields.md) |  | 
**machine** | [**Benefit2Fields**](Benefit2Fields.md) |  | [optional] 

## Example

```python
from datasheets_openapi_client.models.benefits import Benefits

# TODO update the JSON string below
json = "{}"
# create an instance of Benefits from a JSON string
benefits_instance = Benefits.from_json(json)
# print the JSON string representation of the object
print Benefits.to_json()

# convert the object into a dict
benefits_dict = benefits_instance.to_dict()
# create an instance of Benefits from a dict
benefits_form_dict = benefits.from_dict(benefits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


