# warg_openapi.FetchApi

All URIs are relative to *http://localhost:8090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_logs**](FetchApi.md#fetch_logs) | **POST** /fetch/logs | Fetch registry logs
[**fetch_names**](FetchApi.md#fetch_names) | **POST** /fetch/names | Fetch package names
[**get_checkpoint**](FetchApi.md#get_checkpoint) | **GET** /fetch/checkpoint | Fetch latest registry checkpoint


# **fetch_logs**
> FetchLogsResponse fetch_logs(fetch_logs_request, warg_registry=warg_registry)

Fetch registry logs

Fetch the operator and packages logs from the registry.


### Example

```python
import time
import os
import warg_openapi
from warg_openapi.models.fetch_logs_request import FetchLogsRequest
from warg_openapi.models.fetch_logs_response import FetchLogsResponse
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
    api_instance = warg_openapi.FetchApi(api_client)
    fetch_logs_request = warg_openapi.FetchLogsRequest() # FetchLogsRequest | 
    warg_registry = 'registry.example.com' # str | If present and supported, this registry responds on behalf of the other registry specified in this header value. (optional)

    try:
        # Fetch registry logs
        api_response = api_instance.fetch_logs(fetch_logs_request, warg_registry=warg_registry)
        print("The response of FetchApi->fetch_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FetchApi->fetch_logs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_logs_request** | [**FetchLogsRequest**](FetchLogsRequest.md)|  | 
 **warg_registry** | **str**| If present and supported, this registry responds on behalf of the other registry specified in this header value. | [optional] 

### Return type

[**FetchLogsResponse**](FetchLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The logs were successfully fetched. |  * Warg-Registry -  <br>  |
**404** | A requested entity was not found. |  * Warg-Registry -  <br>  |
**0** | An error occurred when processing the request. |  * Warg-Registry -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_names**
> FetchPackageNamesResponse fetch_names(fetch_package_names_request, warg_registry=warg_registry)

Fetch package names

Fetch the package names for registry log IDs.


### Example

```python
import time
import os
import warg_openapi
from warg_openapi.models.fetch_package_names_request import FetchPackageNamesRequest
from warg_openapi.models.fetch_package_names_response import FetchPackageNamesResponse
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
    api_instance = warg_openapi.FetchApi(api_client)
    fetch_package_names_request = warg_openapi.FetchPackageNamesRequest() # FetchPackageNamesRequest | 
    warg_registry = 'registry.example.com' # str | If present and supported, this registry responds on behalf of the other registry specified in this header value. (optional)

    try:
        # Fetch package names
        api_response = api_instance.fetch_names(fetch_package_names_request, warg_registry=warg_registry)
        print("The response of FetchApi->fetch_names:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FetchApi->fetch_names: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_package_names_request** | [**FetchPackageNamesRequest**](FetchPackageNamesRequest.md)|  | 
 **warg_registry** | **str**| If present and supported, this registry responds on behalf of the other registry specified in this header value. | [optional] 

### Return type

[**FetchPackageNamesResponse**](FetchPackageNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The package names were successfully fetched. |  * Warg-Registry -  <br>  |
**404** | A requested entity was not found. |  * Warg-Registry -  <br>  |
**0** | An error occurred when processing the request. |  * Warg-Registry -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkpoint**
> SignedCheckpoint get_checkpoint(warg_registry=warg_registry)

Fetch latest registry checkpoint

Fetch the latest checkpoint from the registry.

### Example

```python
import time
import os
import warg_openapi
from warg_openapi.models.signed_checkpoint import SignedCheckpoint
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
    api_instance = warg_openapi.FetchApi(api_client)
    warg_registry = 'registry.example.com' # str | If present and supported, this registry responds on behalf of the other registry specified in this header value. (optional)

    try:
        # Fetch latest registry checkpoint
        api_response = api_instance.get_checkpoint(warg_registry=warg_registry)
        print("The response of FetchApi->get_checkpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FetchApi->get_checkpoint: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warg_registry** | **str**| If present and supported, this registry responds on behalf of the other registry specified in this header value. | [optional] 

### Return type

[**SignedCheckpoint**](SignedCheckpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The checkpoint was successfully fetched. |  * Warg-Registry -  <br>  |
**0** | An error occurred when processing the request. |  * Warg-Registry -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

