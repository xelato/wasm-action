# warg_openapi.ProofApi

All URIs are relative to *http://localhost:8090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prove_consistency**](ProofApi.md#prove_consistency) | **POST** /proof/consistency | Prove registry checkpoint consistency
[**prove_inclusion**](ProofApi.md#prove_inclusion) | **POST** /proof/inclusion | Prove log leaf inclusion


# **prove_consistency**
> ProveConsistencyResponse prove_consistency(prove_consistency_request=prove_consistency_request)

Prove registry checkpoint consistency

Proves the consistency of the registry between two specified checkpoints.


### Example

```python
import time
import os
import warg_openapi
from warg_openapi.models.prove_consistency_request import ProveConsistencyRequest
from warg_openapi.models.prove_consistency_response import ProveConsistencyResponse
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
    api_instance = warg_openapi.ProofApi(api_client)
    prove_consistency_request = warg_openapi.ProveConsistencyRequest() # ProveConsistencyRequest |  (optional)

    try:
        # Prove registry checkpoint consistency
        api_response = api_instance.prove_consistency(prove_consistency_request=prove_consistency_request)
        print("The response of ProofApi->prove_consistency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofApi->prove_consistency: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prove_consistency_request** | [**ProveConsistencyRequest**](ProveConsistencyRequest.md)|  | [optional] 

### Return type

[**ProveConsistencyResponse**](ProveConsistencyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The consistency proof was generated successfully. |  -  |
**404** | A requested entity was not found. |  -  |
**422** | The proof bundle could not be generated. |  -  |
**0** | An error occurred when processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prove_inclusion**
> ProveInclusionResponse prove_inclusion(prove_inclusion_request=prove_inclusion_request)

Prove log leaf inclusion

Proves that the given log leafs are present in the given registry checkpoint.


### Example

```python
import time
import os
import warg_openapi
from warg_openapi.models.prove_inclusion_request import ProveInclusionRequest
from warg_openapi.models.prove_inclusion_response import ProveInclusionResponse
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
    api_instance = warg_openapi.ProofApi(api_client)
    prove_inclusion_request = warg_openapi.ProveInclusionRequest() # ProveInclusionRequest |  (optional)

    try:
        # Prove log leaf inclusion
        api_response = api_instance.prove_inclusion(prove_inclusion_request=prove_inclusion_request)
        print("The response of ProofApi->prove_inclusion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProofApi->prove_inclusion: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prove_inclusion_request** | [**ProveInclusionRequest**](ProveInclusionRequest.md)|  | [optional] 

### Return type

[**ProveInclusionResponse**](ProveInclusionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The inclusion proof was generated successfully. |  -  |
**404** | A requested entity was not found. |  -  |
**422** | The proof bundle could not be generated. |  -  |
**0** | An error occurred when processing the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

