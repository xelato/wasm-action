# warg_openapi.LedgerApi

All URIs are relative to *http://localhost:8090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ledger_sources**](LedgerApi.md#get_ledger_sources) | **GET** /ledger | Fetch ledger sources


# **get_ledger_sources**
> LedgerSourcesResponse get_ledger_sources(warg_registry=warg_registry)

Fetch ledger sources

Fetch the registry ledger download URL sources.

### Example

```python
import time
import os
import warg_openapi
from warg_openapi.models.ledger_sources_response import LedgerSourcesResponse
from warg_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = warg_openapi.Configuration(
    host = "http://localhost:8090/v1"
)


# Enter a context with an instance of the API client
with warg_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = warg_openapi.LedgerApi(api_client)
    warg_registry = 'registry.example.com' # str | If present and supported, this registry responds on behalf of the other registry specified in this header value. (optional)

    try:
        # Fetch ledger sources
        api_response = api_instance.get_ledger_sources(warg_registry=warg_registry)
        print("The response of LedgerApi->get_ledger_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerApi->get_ledger_sources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warg_registry** | **str**| If present and supported, this registry responds on behalf of the other registry specified in this header value. | [optional] 

### Return type

[**LedgerSourcesResponse**](LedgerSourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ledger sources was successfully fetched. |  * Warg-Registry -  <br>  |
**0** | An error occurred when processing the request. |  * Warg-Registry -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

