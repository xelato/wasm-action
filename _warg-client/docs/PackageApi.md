# _warg_client.PackageApi

All URIs are relative to *http://localhost:8090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_package_record**](PackageApi.md#get_package_record) | **GET** /package/{logId}/record/{recordId} | Get package record status
[**publish_package_record**](PackageApi.md#publish_package_record) | **POST** /package/{logId}/record | Publish package record


# **get_package_record**
> PackageRecord get_package_record(log_id, record_id)

Get package record status

Gets package record status from the registry.

A package record is in one of the following states:
  * `sourcing`: The package record needs content sources.
  * `processing`: The package record is being processed.
  * `rejected`: The package record was rejected.
  * `published`: The package record was published to the log.


### Example

```python
import time
import os
import _warg_client
from _warg_client.models.package_record import PackageRecord
from _warg_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = _warg_client.Configuration(
    host = "http://localhost:8090/v1"
)


# Enter a context with an instance of the API client
with _warg_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = _warg_client.PackageApi(api_client)
    log_id = 'log_id_example' # str | The package log identifier.
    record_id = 'record_id_example' # str | The record identifier.

    try:
        # Get package record status
        api_response = api_instance.get_package_record(log_id, record_id)
        print("The response of PackageApi->get_package_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->get_package_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_id** | **str**| The package log identifier. | 
 **record_id** | **str**| The record identifier. | 

### Return type

[**PackageRecord**](PackageRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The package record. |  -  |
**404** | A requested entity was not found. |  -  |
**0** | An error occurred when processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_package_record**
> PackageRecord publish_package_record(log_id, publish_package_record_request)

Publish package record

Attempts to publish a new record to a package log.

Publishing package records is an asynchronous operation.

The record must be signed by a key that is authorized to modify the package log.


### Example

```python
import time
import os
import _warg_client
from _warg_client.models.package_record import PackageRecord
from _warg_client.models.publish_package_record_request import PublishPackageRecordRequest
from _warg_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8090/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = _warg_client.Configuration(
    host = "http://localhost:8090/v1"
)


# Enter a context with an instance of the API client
with _warg_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = _warg_client.PackageApi(api_client)
    log_id = 'log_id_example' # str | The package log identifier.
    publish_package_record_request = _warg_client.PublishPackageRecordRequest() # PublishPackageRecordRequest | 

    try:
        # Publish package record
        api_response = api_instance.publish_package_record(log_id, publish_package_record_request)
        print("The response of PackageApi->publish_package_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageApi->publish_package_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_id** | **str**| The package log identifier. | 
 **publish_package_record_request** | [**PublishPackageRecordRequest**](PublishPackageRecordRequest.md)|  | 

### Return type

[**PackageRecord**](PackageRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The package record was accepted. |  -  |
**401** | Unauthorized rejection from the registry.  |  -  |
**404** | A requested entity was not found. |  -  |
**409** | The requested package publish conflicts. |  -  |
**422** | The package was rejected by the registry.  |  -  |
**501** | The server does not support publishing package records with explicitly specified content source locations.  |  -  |
**0** | An error occurred when processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

