# warg_openapi.MonitorApi

All URIs are relative to *http://localhost:8090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_checkpoint**](MonitorApi.md#verify_checkpoint) | **POST** /verify/checkpoint | Verify registry checkpoint


# **verify_checkpoint**
> CheckpointVerificationResponse verify_checkpoint(signed_checkpoint=signed_checkpoint)

Verify registry checkpoint

Verify checkpoint from the registry. The client must interpret the response body to determine the verification status.

### Example

```python
import time
import os
import warg_openapi
from warg_openapi.models.checkpoint_verification_response import CheckpointVerificationResponse
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
    api_instance = warg_openapi.MonitorApi(api_client)
    signed_checkpoint = warg_openapi.SignedCheckpoint() # SignedCheckpoint |  (optional)

    try:
        # Verify registry checkpoint
        api_response = api_instance.verify_checkpoint(signed_checkpoint=signed_checkpoint)
        print("The response of MonitorApi->verify_checkpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->verify_checkpoint: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signed_checkpoint** | [**SignedCheckpoint**](SignedCheckpoint.md)|  | [optional] 

### Return type

[**CheckpointVerificationResponse**](CheckpointVerificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The checkpoint verification request was processed. The client must interpret the response body to determine the verification status. |  -  |
**0** | An error occurred when processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

