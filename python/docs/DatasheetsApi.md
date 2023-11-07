# datasheets_openapi_client.DatasheetsApi

All URIs are relative to *http://kitt4sme.collab-cloud.eu/datasheets-backend-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasheets_get**](DatasheetsApi.md#datasheets_get) | **GET** /datasheets | Returns validated datasheets


# **datasheets_get**
> ApiResponse datasheets_get(validate)

Returns validated datasheets

Returns a list of datasheets that have been validated by market place

### Example

```python
import time
import os
import datasheets_openapi_client
from datasheets_openapi_client.models.api_response import ApiResponse
from datasheets_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://kitt4sme.collab-cloud.eu/datasheets-backend-rest
# See configuration.py for a list of all supported configuration parameters.
configuration = datasheets_openapi_client.Configuration(
    host = "http://kitt4sme.collab-cloud.eu/datasheets-backend-rest"
)


# Enter a context with an instance of the API client
with datasheets_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = datasheets_openapi_client.DatasheetsApi(api_client)
    validate = 56 # int | 1 or 0 if the datasheet is to be validated against the marketplace

    try:
        # Returns validated datasheets
        api_response = api_instance.datasheets_get(validate)
        print("The response of DatasheetsApi->datasheets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasheetsApi->datasheets_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate** | **int**| 1 or 0 if the datasheet is to be validated against the marketplace | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

