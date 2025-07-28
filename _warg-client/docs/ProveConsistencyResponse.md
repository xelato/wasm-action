# ProveConsistencyResponse

A response containing the consistency proof bundle.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proof** | **bytearray** | The consistency proof bundle. | 

## Example

```python
from _warg_client.models.prove_consistency_response import ProveConsistencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProveConsistencyResponse from a JSON string
prove_consistency_response_instance = ProveConsistencyResponse.from_json(json)
# print the JSON string representation of the object
print ProveConsistencyResponse.to_json()

# convert the object into a dict
prove_consistency_response_dict = prove_consistency_response_instance.to_dict()
# create an instance of ProveConsistencyResponse from a dict
prove_consistency_response_from_dict = ProveConsistencyResponse.from_dict(prove_consistency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


