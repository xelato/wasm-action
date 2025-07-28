# CheckpointVerificationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkpoint** | **str** | The verification of the checkpoint&#39;s &#x60;logLength&#x60;, &#x60;logRoot&#x60; and &#x60;mapRoot&#x60;:    * &#x60;unverified&#x60;: checkpoint may be valid or invalid; if &#x60;retryAfter&#x60; is provided, the client should retry the request;   * &#x60;verified&#x60;: &#x60;logLength&#x60;, &#x60;logRoot&#x60; and &#x60;mapRoot&#x60; are verified;   * &#x60;invalid&#x60;: checkpoint with the specified &#x60;logLength&#x60; was either not produced or does not match the correct &#x60;logRoot&#x60; and &#x60;mapRoot&#x60;;  | 
**signature** | **str** | The verification of the checkpoint&#39;s &#x60;keyId&#x60; and &#x60;signature&#x60;:    * &#x60;unverified&#x60;: checkpoint&#39;s &#x60;signature&#x60; may be valid or invalid; if &#x60;retryAfter&#x60; is provided, the client should retry the request;   * &#x60;verified&#x60;: checkpoint&#39;s &#x60;signature&#x60; is verified;   * &#x60;invalid&#x60;: &#x60;keyId&#x60; is not known or does not have authorization (could have been revoke or never granted) to sign checkpoints or the &#x60;signature&#x60; itself is invalid;  | 
**retry_after** | **int** | If either &#x60;checkpoint&#x60; or &#x60;signature&#x60; is &#x60;unverified&#x60; status, then the server may instruct the client to retry the request after the specified number of seconds. | [optional] 

## Example

```python
from warg_openapi.models.checkpoint_verification_response import CheckpointVerificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckpointVerificationResponse from a JSON string
checkpoint_verification_response_instance = CheckpointVerificationResponse.from_json(json)
# print the JSON string representation of the object
print CheckpointVerificationResponse.to_json()

# convert the object into a dict
checkpoint_verification_response_dict = checkpoint_verification_response_instance.to_dict()
# create an instance of CheckpointVerificationResponse from a dict
checkpoint_verification_response_from_dict = CheckpointVerificationResponse.from_dict(checkpoint_verification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


