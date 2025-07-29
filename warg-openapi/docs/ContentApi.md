# warg_openapi.ContentApi

All URIs are relative to *http://localhost:8090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content_sources**](ContentApi.md#get_content_sources) | **GET** /content/{digest} | Get content sources


# **get_content_sources**
> ContentSourcesResponse get_content_sources(digest, warg_registry=warg_registry)

Get content sources

Gets a content sources for the given digest from the registry.


### Example

```python
import time
import os
import warg_openapi
from warg_openapi.models.content_sources_response import ContentSourcesResponse
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
    api_instance = warg_openapi.ContentApi(api_client)
    digest = 'digest_example' # str | The content digest.
    warg_registry = 'registry.example.com' # str | If present and supported, this registry responds on behalf of the other registry specified in this header value. (optional)

    try:
        # Get content sources
        api_response = api_instance.get_content_sources(digest, warg_registry=warg_registry)
        print("The response of ContentApi->get_content_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentApi->get_content_sources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **digest** | **str**| The content digest. | 
 **warg_registry** | **str**| If present and supported, this registry responds on behalf of the other registry specified in this header value. | [optional] 

### Return type

[**ContentSourcesResponse**](ContentSourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The content digest sources. |  * Warg-Registry -  <br>  |
**404** | A requested entity was not found. |  * Warg-Registry -  <br>  |
**0** | An error occurred when processing the request. |  * Warg-Registry -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

